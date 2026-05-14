# Image2 Prompts

Use these prompts to replace the SVG fallback with high-fidelity image2 assets.

## Execution Priority

1. In a Codex session with a built-in image generation tool, call that tool directly. It does not require the local `OPENAI_API_KEY`.
2. Use the local `imagegen` CLI only for reproducible batch generation, scripted runs, or explicit API-parameter control.
3. If using the local CLI, expect it to require `OPENAI_API_KEY` and local dependencies.

Do not block repo art generation just because the local CLI environment is missing a key. That was a failure mode observed during this repo setup.

## Social Card

```text
Use case: infographic-diagram
Asset type: GitHub repository social preview image, 1200x630
Primary request: a restrained cross-domain academic research visual for a skill named "Academic Paper Figure Image2"
Scene/background: clean ivory paper background with subtle printed-paper texture, thin black border, undergraduate thesis figure motifs across multiple fields
Subject: traditional thesis visuals: black-and-white software ER/DFD and flowcharts, plus restrained print-safe data charts for modeling, questionnaires, finance indicators, and experiment results, small audit checklist marks
Style/medium: high-end editorial academic illustration, conservative Chinese undergraduate thesis aesthetic, precise vector-like linework, field-appropriate textbook symbols
Composition/framing: wide landscape card, title area on top-left, diagram pipeline across the center, enough negative space, no clutter
Lighting/mood: calm, rigorous, archival, research-grade
Color palette: ivory, black, warm gray, very subtle muted blue accents only if needed
Text: "Academic Paper Figure Image2" and "Research-first figure audit"
Constraints: no cartoon mascot, no neon, no SaaS dashboard style, no fake UI, no watermark, no internal figure caption, no real school name, no real student name, no real thesis title, no real student ID, all text must be readable
```

## README Hero

```text
Use case: infographic-diagram
Asset type: README hero image, 1536x768
Primary request: a conservative academic workflow illustration showing thesis evidence research, cross-domain figure audit, image2 prompting, and final textbook-style figures
Style/medium: scholarly academic diagram, clean line art, black-and-white structural symbols, restrained print-safe color only for data charts, traditional undergraduate textbook conventions for software, modeling, data analysis, survey research, management, and finance
Composition/framing: left-to-right workflow, spacious, suitable for GitHub README
Constraints: no colorful modern architecture icons, no Mermaid/TikZ look, no captions inside diagram, no watermark, no real school name, no real student name, no real thesis title, no real student ID
```
