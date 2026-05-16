#!/usr/bin/env python3
"""Audit thesis figure assets before and after image2 upgrades.

The script is intentionally conservative: it inventories files, dimensions,
aspect ratios, and obvious SVG font risks. It can also build a contact sheet
when Pillow is available, which gives reviewers a fast visual regression pass
without opening every figure one by one.
"""

from __future__ import annotations

import argparse
import html
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".svg"}
SVG_FONT_RISK_RE = re.compile(
    r"(SimSun|Songti|STSong|Microsoft YaHei|Arial|Helvetica|PingFang|Heiti|sans-serif)",
    re.IGNORECASE,
)
SVG_CJK_FONT_RE = re.compile(r"(KaiTi_GB2312|KaiTi|STKaiti|楷体)", re.IGNORECASE)
SVG_LATIN_FONT_RE = re.compile(r"(Times New Roman|Times|STIX|Cambria Math)", re.IGNORECASE)


@dataclass
class Asset:
    path: Path
    width: int | None
    height: int | None
    source_kind: str
    flags: list[str]

    @property
    def aspect(self) -> float | None:
        if not self.width or not self.height:
            return None
        return round(self.width / self.height, 3)


def is_skipped_path(path: Path, root: Path, include_backups: bool) -> bool:
    rel_parts = path.relative_to(root).parts
    for part in rel_parts[:-1]:
        lower = part.lower()
        if lower.startswith("."):
            return True
        if not include_backups and ("backup" in lower or lower in {"bak", "old"}):
            return True
    return False


def iter_images(root: Path, recursive: bool, include_backups: bool) -> Iterable[Path]:
    pattern = "**/*" if recursive else "*"
    for path in sorted(root.glob(pattern)):
        if is_skipped_path(path, root, include_backups):
            continue
        if path.is_file() and path.suffix.lower() in IMAGE_EXTS:
            yield path


def raster_size(path: Path) -> tuple[int | None, int | None]:
    try:
        from PIL import Image
    except Exception:
        return None, None

    try:
        with Image.open(path) as image:
            return image.size
    except Exception:
        return None, None


def svg_size_and_flags(path: Path) -> tuple[int | None, int | None, list[str]]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    width = height = None

    width_match = re.search(r'\bwidth=["\']([0-9.]+)', text)
    height_match = re.search(r'\bheight=["\']([0-9.]+)', text)
    if width_match and height_match:
        width = int(float(width_match.group(1)))
        height = int(float(height_match.group(1)))
    else:
        viewbox_match = re.search(r'\bviewBox=["\']\s*[-0-9.]+\s+[-0-9.]+\s+([0-9.]+)\s+([0-9.]+)', text)
        if viewbox_match:
            width = int(float(viewbox_match.group(1)))
            height = int(float(viewbox_match.group(2)))

    flags: list[str] = []
    if SVG_FONT_RISK_RE.search(text):
        flags.append("svg_font_risk")
    if not SVG_CJK_FONT_RE.search(text):
        flags.append("missing_kaiti_hint")
    if not SVG_LATIN_FONT_RE.search(text):
        flags.append("missing_times_hint")
    return width, height, flags


def classify(path: Path) -> str:
    name = path.name.lower()
    tokens = set(re.split(r"[^a-z0-9]+", path.stem.lower()))
    if path.suffix.lower() == ".svg":
        return "code-chart/svg"
    if tokens & {"screenshot", "screen", "ui", "interface"}:
        return "screenshot"
    if tokens & {"chart", "metrics", "bar", "line", "plot"}:
        return "data-visualization"
    return "image2-or-diagram"


def audit_asset(path: Path) -> Asset:
    flags: list[str] = []
    if path.suffix.lower() == ".svg":
        width, height, svg_flags = svg_size_and_flags(path)
        flags.extend(svg_flags)
    else:
        width, height = raster_size(path)

    if width and height:
        if width < 1000 or height < 600:
            flags.append("low_resolution_for_a4")
        aspect = width / height
        if aspect > 2.4:
            flags.append("very_wide_check_readability")
        if aspect < 0.45:
            flags.append("very_tall_check_page_fit")
    else:
        flags.append("dimension_unknown")

    return Asset(path=path, width=width, height=height, source_kind=classify(path), flags=flags)


def write_markdown(assets: list[Asset], root: Path, out_md: Path) -> None:
    lines = [
        "# Figure Asset Audit",
        "",
        f"Root: `{root}`",
        "",
        "| File | Kind | Size | Aspect | Flags |",
        "| --- | --- | --- | --- | --- |",
    ]
    for asset in assets:
        rel = asset.path.relative_to(root)
        size = f"{asset.width}x{asset.height}" if asset.width and asset.height else "unknown"
        aspect = f"{asset.aspect:.3f}" if asset.aspect else "unknown"
        flags = ", ".join(asset.flags) if asset.flags else "ok"
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{html.escape(str(rel))}`",
                    asset.source_kind,
                    size,
                    aspect,
                    flags,
                ]
            )
            + " |"
        )
    lines.append("")
    lines.append("## Review Rules")
    lines.append("")
    lines.append("- Fix `svg_font_risk` in chart source before rendering final figures.")
    lines.append("- Inspect `very_wide_check_readability` and `very_tall_check_page_fit` in compiled PDF/Word pages.")
    lines.append("- Back up image2 assets before replacing them with edited Codex/image2 outputs.")
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_contact_sheet(assets: list[Asset], out_path: Path, thumb_width: int) -> None:
    try:
        from PIL import Image, ImageDraw, ImageFont
    except Exception as exc:
        raise SystemExit(f"contact sheet requires Pillow: {exc}") from exc

    raster_assets = [asset for asset in assets if asset.path.suffix.lower() != ".svg"]
    if not raster_assets:
        raise SystemExit("no raster images available for contact sheet")

    cols = 3
    label_h = 54
    padding = 18
    cells: list[tuple[Asset, Image.Image]] = []
    for asset in raster_assets:
        with Image.open(asset.path) as image:
            image = image.convert("RGB")
            scale = thumb_width / image.width
            thumb_h = max(1, int(image.height * scale))
            image = image.resize((thumb_width, thumb_h))
            cells.append((asset, image))

    cell_w = thumb_width + padding * 2
    cell_h = max(image.height for _, image in cells) + label_h + padding * 2
    rows = (len(cells) + cols - 1) // cols
    sheet = Image.new("RGB", (cell_w * cols, cell_h * rows), "white")
    draw = ImageDraw.Draw(sheet)
    try:
        font = ImageFont.truetype("Arial Unicode.ttf", 16)
    except Exception:
        font = ImageFont.load_default()

    for index, (asset, image) in enumerate(cells):
        row, col = divmod(index, cols)
        x = col * cell_w + padding
        y = row * cell_h + padding
        sheet.paste(image, (x, y))
        label = f"{asset.path.name}  {asset.width or '?'}x{asset.height or '?'}"
        draw.text((x, y + image.height + 8), label[:80], fill=(0, 0, 0), font=font)
        if asset.flags:
            draw.text((x, y + image.height + 30), ", ".join(asset.flags)[:80], fill=(160, 0, 0), font=font)

    sheet.save(out_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit academic thesis figure assets.")
    parser.add_argument("root", type=Path, help="directory containing figure assets")
    parser.add_argument("--recursive", action="store_true", help="scan directories recursively")
    parser.add_argument("--include-backups", action="store_true", help="include backup/old directories")
    parser.add_argument("--out-md", type=Path, help="write a Markdown audit table")
    parser.add_argument("--contact-sheet", type=Path, help="write a raster-image contact sheet")
    parser.add_argument("--thumb-width", type=int, default=420, help="contact-sheet thumbnail width")
    args = parser.parse_args()

    root = args.root.expanduser().resolve()
    if not root.exists():
        raise SystemExit(f"root does not exist: {root}")

    assets = [audit_asset(path) for path in iter_images(root, args.recursive, args.include_backups)]
    if args.out_md:
        write_markdown(assets, root, args.out_md.expanduser().resolve())
    if args.contact_sheet:
        write_contact_sheet(assets, args.contact_sheet.expanduser().resolve(), args.thumb_width)

    print(f"audited {len(assets)} figure assets under {root}")
    for asset in assets:
        flags = ", ".join(asset.flags) if asset.flags else "ok"
        size = f"{asset.width}x{asset.height}" if asset.width and asset.height else "unknown"
        print(f"- {asset.path.name}: {asset.source_kind}, {size}, {flags}")


if __name__ == "__main__":
    main()
