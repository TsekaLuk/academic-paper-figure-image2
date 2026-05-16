---
name: academic-paper-figure-image2
description: Research, audit, redesign, generate, review, and place high-resolution traditional academic figures for Chinese undergraduate and adult-education theses using image-generation models. Use when a thesis needs field-appropriate conservative figures or tables, including software-engineering DFD/ER/flow/module diagrams, math-modeling model-flow/sensitivity/error diagrams, data-analysis cleaning/statistical/model-evaluation charts, market-research questionnaire/sample/crosstab visuals, management fishbone/SWOT/PEST/process diagrams, education-research survey/interview/statistical visuals, or finance/accounting indicator/trend/comparison charts. Also use when existing mock, missing, Mermaid, TikZ, code-generated, modern, oversized, cluttered, or crude figures need to be audited, replaced, or added for conservative thesis reviewers.
---

# Academic Paper Figure Image2

## Core Rule

Optimize for thesis approval, not visual novelty. Produce conservative, textbook-style figures that match the target field's undergraduate thesis conventions. Use black-and-white by default for structural diagrams such as DFD, ER, module, architecture, flowchart, and sequence diagrams. For data visualizations such as bar charts, line charts, scatter plots, correlation charts, distribution charts, sensitivity/error charts, survey charts, and finance indicator charts, restrained academic color is allowed when it improves comparison and readability.

Do not generate trendy architecture posters, colorful product diagrams, UI mockups, or Mermaid/TikZ-looking output. Do not put the figure caption inside the image. The paper or document system should own captions and numbering.

Never start from image generation. Start from understanding the thesis type, accepted sample theses, source data/materials, implementation or research method, and the reviewer-facing argument. A correct boring figure beats a beautiful false figure.

## Workflow

1. Research the thesis topic, domain type, chapter structure, accepted reference theses, and school format rules.
2. Inspect the real evidence: source code, data tables, questionnaires, interview outlines, model formulas, case materials, financial statements, experiment records, screenshots, or test artifacts.
3. Convert the evidence into a field-friendly explanation model: requirements/design for software, assumptions/model/solution for modeling, data/source/method/result for analysis, questionnaire/sample/statistics for survey work, framework/problem/countermeasure for management cases.
4. Audit existing figures and mark mock diagrams, Mermaid/TikZ figures, code-generated charts, modern architecture posters, oversized diagrams, and misplaced figures for replacement.
5. Audit missing figures: identify chapters where a本科论文 normally needs a diagram but the text only uses plain narration.
6. Choose the traditional figure or table type expected in the target chapter and field.
7. Reduce the figure to stable textbook symbols and short Chinese labels.
8. Write a COSTAR image prompt with strict composition constraints.
9. Generate one figure at a time, preferably landscape if it contains many nodes.
10. Inspect for academic legibility: no cropped nodes, no crossing arrows, no decorative styling, no caption in the image.
11. Insert the image near the paragraph that first introduces it, then add a normal thesis caption outside the image.

For the full audit-and-upgrade workflow, load [references/research-audit-workflow.md](references/research-audit-workflow.md). For non-software fields, load [references/cross-domain-figure-playbook.md](references/cross-domain-figure-playbook.md).

## Pre-Generation Research

Before writing prompts, gather enough evidence to avoid making decorative but inaccurate diagrams:

- Thesis structure: chapter titles, section goals, figure numbering, and chapter-summary style.
- Accepted examples: what diagrams appear in the same chapter of approved theses, especially adult-education or second-degree theses.
- System implementation: source-code directory tree, routes/pages, service modules, database schema, API contracts, storage objects, export/import flows, and test/demo paths.
- Paper narrative: how the author explains the work in the field's conservative undergraduate language.
- Existing diagram inventory: figure filename, caption, source type, chapter location, and replacement decision.
- Missing-figure inventory: sections with long prose descriptions but no diagram, especially requirements, overall design, database design, implementation process, and testing.
- Domain-material inventory: sections where the field normally expects a table, chart, model diagram, variable list, sample profile, reliability/validity table, indicator system, or countermeasure matrix.

Treat source code, data, questionnaires, models, and case materials as evidence, then translate them into thesis language. For example, a Next.js route becomes a "前端页面模块"; a survey sheet becomes a "样本统计表"; a formula group becomes a "模型建立过程"; a financial statement becomes a "指标分析数据来源".

## Figure Audit and Replacement Rules

Replace or redesign figures when any of these are true:

- The figure is a mock placeholder that does not reflect the actual system.
- The figure is generated directly from Mermaid/TikZ/code and looks cramped, mechanical, inappropriately colorful for its figure type, or visually inconsistent with a thesis.
- The figure contains hover boxes, UI artifacts, code labels, markdown, internal captions, or accidental tool output.
- The diagram type is placed in the wrong chapter, such as ER diagrams in requirements analysis or deployment diagrams before overall design.
- The ER diagram is too shallow and only lists a few entities without attributes or cardinalities.
- The DFD is actually a modern service dependency graph and lacks external entities, processes, data stores, or data-flow direction.
- The flowchart exceeds the page, has crossing arrows, or lacks start/end and decision branch labels.

Do not "patch" bad diagrams by shrinking them. Rebuild the content model, split the figure if needed, then regenerate.

## Missing Figure Audit

Add new figures when a conservative本科论文 reviewer would expect visual proof but the thesis only uses prose. This is as important as replacing bad figures.

Look for these signals:

- Requirements analysis explains users, roles, or业务流程 for more than a few paragraphs but has no use-case diagram, business flowchart, or context DFD.
- Overall design describes modules, architecture, data movement, or storage but has no module diagram, architecture diagram, or DFD.
- Database design lists tables or entities but has no complete ER diagram and no entity subgraphs.
- Implementation chapter describes import, editing, collaboration, export, review, login, or administration flows but has no flowchart or system screenshot.
- Testing chapter lists test cases but has no test process, scenario flow, or result screenshot.
- A section repeatedly says "系统实现了..." without a diagram proving how the system works.

When adding missing figures, do not add decorative filler. Each added figure must resolve a review risk: unclear requirements, weak design evidence, thin database design, unconvincing implementation, or insufficient testing proof.

Default minimum figure set for a software system-design undergraduate thesis:

- Requirements: use-case diagram or业务流程图, plus context/level-0 DFD if data movement matters.
- Overall design: system architecture diagram, functional module diagram, and main data-flow diagram.
- Database/detailed design: overall ER diagram plus sub-ER diagrams for crowded core entities.
- Implementation: key business process flowcharts and several real system screenshots.
- Testing: test flow or test scenario diagram plus test case/result tables.

## Chapter Placement Rules

Use figures where an older field reviewer expects them. The exact expected object changes by discipline; do not force software diagrams into non-software papers.

| Chapter area | Preferred figures | Avoid |
| --- | --- | --- |
| Introduction | Rarely use diagrams; use only if explaining research route | Complex system diagrams before requirements |
| Requirements analysis | Business flowchart, use-case diagram, context DFD, level-0 DFD, data dictionary table | Database ER diagrams, deployment topology |
| Overall design | System architecture, functional module structure, data flow, database conceptual model | Page screenshots as the main evidence |
| Detailed design / database design | Full ER diagram plus entity subgraphs, table relation diagram, core algorithm/process flow | One tiny ER diagram with only 3-4 entities |
| Implementation | Key module flowcharts, interface screenshots, import/export process, user operation process | Abstract methodology diagrams |
| Testing / application effect | Test process, scenario flow, result screenshots, test case tables | New architecture diagrams |
| Appendix | Large grammar, code, extra tables, oversized diagrams | Main proof figures that the正文 depends on |

Each chapter should have a numbered chapter summary if the thesis style uses chapter summaries. Keep figures near their corresponding section instead of collecting them randomly.

For cross-domain placement rules, load [references/cross-domain-figure-playbook.md](references/cross-domain-figure-playbook.md).

When upgrading an existing thesis, first create a figure map:

| Existing figure | Current chapter | Problem | Replacement type | Target chapter |
| --- | --- | --- | --- | --- |
| mock architecture | requirements | wrong abstraction | context DFD | requirements |
| Mermaid ER | design | too simple | full ER + sub-ER | database design |
| TikZ data flow | design | cluttered/crossing arrows | traditional DFD | overall design |

Also create a missing-figure map:

| Section | Prose-only claim | Risk | Added figure |
| --- | --- | --- | --- |
| requirements | describes actors and operations | requirements look unsupported | use-case diagram |
| overall design | describes modules in text | design looks thin | module hierarchy |
| database design | lists tables only | database design looks incomplete | ER subgraph |
| implementation | describes export process | implementation lacks proof | export flowchart |

## Traditional Style Requirements

Use these visual constraints unless the user gives a stricter school template:

- White background, black or dark-gray lines, no gradients, no shadows, no icons unless required by the diagram convention.
- Use the figure type to choose color:
  - Structural diagrams should stay black-and-white or grayscale unless the school/sample thesis clearly uses a restrained accent.
  - Data visualizations may use a limited, print-safe academic palette when color clarifies series, groups, categories, or thresholds.
  - Prefer 2-5 muted, high-contrast colors; also use labels, line styles, markers, or hatching so the chart remains understandable when printed in grayscale.
  - Avoid rainbow palettes, neon colors, gradients, translucent dashboard fills, decorative backgrounds, and color-only encodings without labels or legend.
- Follow the target school's figure typography when it is known. For Jiangsu Ocean University-style Chinese thesis body figures and tables, use 五号 KaiTi_GB2312 for Chinese labels and 五号 Times New Roman, or another academic serif only when Times is unavailable, for English letters, model names, numbers, and formulas.
- If no school-specific font rule is known, use Songti/SimSun-like Chinese labels if possible and English labels in Times-like serif if needed.
- Thin, consistent strokes; right-angle or straight arrows; no hover boxes, floating decorations, or canvas artifacts.
- Nodes arranged on a clear grid with generous spacing.
- Labels short enough to fit: usually 2-8 Chinese characters per node.
- Image should be high resolution and clean enough for A4 thesis insertion at single-column width.
- Do not include "图 x.x" or explanatory caption text inside the image.

## Font-Only Edit Rule

When the thesis already uses an image2/Codex-generated figure with correct structure, and the defect is typography only, edit the original image with the image model instead of redrawing it with code. Preserve the image's node layout, arrows, grouping, colors, and academic visual language. The edit prompt should say "change only typography" and should explicitly name the required Chinese and English fonts.

Do not replace image2 assets with Python, Pillow, Matplotlib, SVG, TikZ, Mermaid, or other code-rendered diagrams merely to satisfy font requirements. Code-generated charts remain appropriate for data-driven visualizations, but image2 diagram assets should stay image-model-authored unless the user explicitly asks for a code-rendered replacement.

### Codex Built-In Image Editing

In Codex desktop sessions, prefer the built-in Codex image-generation/editing tool for image2 work. Do not treat a missing local `OPENAI_API_KEY` as a blocker when Codex image capability is available; the local `imagegen` CLI is only an optional reproducible fallback for environments without built-in image editing.

When using Codex built-in image editing, edit the existing image2 asset itself when the structure is already correct. Do not regenerate from a text prompt just to fix typography, because regenerated diagrams often drift in logic, arrows, labels, or node ordering. The workflow is:

1. open or attach the original image2 figure;
2. request a font-only edit with explicit invariants;
3. inspect the edited output for structure drift before replacing the thesis asset;
4. copy the generated image from Codex's generated-images cache into the thesis figure path, leaving the original cached output in place.

Codex desktop generated images are normally saved under `~/.codex/generated_images/<session-id>/<image-id>.png`. When moving an edited figure into a thesis repo, copy it to the target figure path instead of deleting or moving the cache file.

## Diagram-Specific Rules

### Data Flow Diagram

Use external entities as rectangles, processes as circles or rounded rectangles, data stores as open-ended rectangles or double-line stores, and arrows for data flow.

The minimum acceptable pattern is:

`外部实体 -> 处理过程 -> 数据存储 / 输出结果`

For requirements chapters, prefer a context DFD plus level-0 DFD. For design chapters, use a refined DFD that names services, databases, files, and output documents.

### ER Diagram

Use rectangles for entities, diamonds for relationships, ovals for attributes, and cardinalities near relationship lines. This is more acceptable to traditional reviewers than a modern UML-style table box.

Do not submit a single underdeveloped ER figure. Create:

- one overall ER diagram with the core entities and relationships;
- 2-4 entity subgraphs if the overall diagram would be too crowded;
- clear cardinalities such as `1`, `N`, `1:N`, `M:N`;
- attributes that demonstrate real database thinking: identifier, name/title, status, time, owner, type, path, permission, version, etc.

### Flowchart

Use terminal ovals, process rectangles, decision diamonds, arrows, and optional document/data symbols. Keep decision labels as questions, and label outgoing branches with `是` and `否`.

If the flow has more than 8-10 nodes, split it into a main process and one subprocess figure.

### Functional Module Diagram

Use hierarchical boxes. Put the system name at the top, major modules in the second row, and submodules below. Avoid diagonal arrows unless explaining dependency; module diagrams are usually structural, not flow-based.

### Architecture / Deployment Diagram

Use layered boxes for client, application service, storage, and external services. Keep it conservative: browser/client, application server, business service, database, file storage, export result.

Avoid cloud-product marketing icons unless the paper is explicitly about cloud architecture and the reviewer accepts them.

### Data Visualization

Use chart types that match the evidence: bar charts for metric comparison, line charts for time trends, scatter plots for correlation, box/distribution charts for dispersion, heatmaps for matrices, and grouped bars or small multiples for survey or strategy comparisons.

Data visualizations do not have to be grayscale. Use restrained academic color when it makes grouped data easier to compare, but keep the chart thesis-like:

- derive every value from the thesis data, experiment output, questionnaire, model result, or financial statement;
- use short axis labels, units, legends, and direct annotations where needed;
- keep the background white and the plotting area clean;
- use print-safe colors plus line styles, markers, hatching, or direct labels so the chart remains legible in black-and-white copies;
- do not use dashboard cards, glowing palettes, 3D effects, pictograms, or decorative infographics.

## COSTAR Prompt Pattern

Use this pattern for each image-model request:

```text
Context: This figure is for a Chinese undergraduate thesis in [field]. It is based on the actual thesis evidence: [source code/data/formulas/questionnaire/case material/financial statements/screenshots]. It must look like a traditional textbook-style academic figure, not a modern poster or product diagram.

Objective: Generate a high-resolution [diagram/chart/table type] for [chapter/section purpose].

Style: Conservative academic style, white background, thin lines, simple geometric symbols or clean chart marks, school-compliant typography, no gradient, no shadow, no decorative icons, no caption inside the image. Use black-and-white for structural diagrams unless the thesis already uses restrained academic accent fills. For data charts, use a restrained print-safe academic palette only when color improves comparison; include labels, markers, line styles, hatching, or legends so the chart is still readable in grayscale. If the school requires it, use 五号 KaiTi_GB2312 for Chinese labels and 五号 Times New Roman for English letters, numbers, and formulas.

Task: Draw the following materials derived from the thesis analysis: [nodes, relationships, variables, indicators, data flows, factors, arrows, cardinalities, branch labels, or table dimensions].

Audience: Conservative undergraduate thesis reviewers who expect standard field-appropriate academic figures.

Response: Output only the diagram image. Ensure all Chinese text is readable, no node is cropped, arrows do not cross boxes, layout fits A4 thesis insertion.
```

For font-only image2 edits, use this stricter edit instruction:

```text
Edit this existing academic thesis figure. Preserve the exact content, nodes, arrows, layout, colors, line style, margins, and overall image2-authored structure. Change only typography: all Chinese labels must use 五号 KaiTi_GB2312; all English letters, model names, numbers, and formulas must use 五号 Times New Roman or an equivalent academic serif. Keep text readable at A4 thesis insertion width. Do not add a caption, figure number, watermark, title outside the diagram, new icons, or extra decoration.
```

For ready-to-use prompts, load [references/prompt-templates.md](references/prompt-templates.md).

## Review Checklist

Reject and regenerate if any item fails:

- The image contains a caption, title like `Figure`, watermark, markdown, or code.
- Chinese labels are garbled, misspelled, too small, or inconsistent.
- Nodes overlap, arrows cross through boxes, or the image is cropped.
- ER diagram lacks attributes or cardinalities.
- DFD lacks external entity, process, data store, or data-flow direction.
- Flowchart lacks start/end or decision branch labels.
- Styling looks modern, decoratively colorful, promotional, or UI-dashboard-like.
- Data visualization uses decorative color, color-only encoding, or an unverifiable chart value.
- The figure is placed in a chapter where its diagram type does not belong.
- A font-only request was handled by redrawing the figure with code instead of editing the original image2 figure.
- Chinese labels violate the required school font, or English/numeric labels use a non-academic sans-serif when Times New Roman is required.

For a stricter handoff checklist, load [references/review-checklist.md](references/review-checklist.md).

## Thesis Editing Notes

If replacing Mermaid/TikZ figures, remove the source diagram block from the thesis and insert the generated image asset. Keep the figure caption outside the image, using the thesis template's normal figure environment.

If replacing a code-generated figure, delete the brittle generation path from the final thesis source unless the project intentionally keeps reproducible figure generation. The submitted thesis should not reveal accidental implementation scaffolding.

If a generated diagram is too large, do not shrink it until unreadable. Split it into a main figure plus subfigures or move the oversized details to an appendix.

If the user says "最能让我毕业", prefer boring completeness over elegance: full DFD, full ER plus sub-ER, standard flowcharts, screenshots in implementation, and chapter-consistent placement.
