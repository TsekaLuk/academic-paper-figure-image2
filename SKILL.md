---
name: academic-paper-figure-image2
description: Research, audit, redesign, generate, review, and place high-resolution traditional academic figures for Chinese adult-education undergraduate computer-science theses using image-generation models. Use when a thesis needs conventional textbook-style data-flow diagrams, ER diagrams, flowcharts, module diagrams, architecture diagrams, deployment diagrams, or when existing mock, Mermaid, TikZ, code-generated, modern, oversized, cluttered, or crude figures need to be upgraded for conservative thesis reviewers.
---

# Academic Paper Figure Image2

## Core Rule

Optimize for thesis approval, not visual novelty. Produce conservative, black-and-white, textbook-style computer-science diagrams that look like they belong in an adult-education undergraduate thesis.

Do not generate trendy architecture posters, colorful product diagrams, UI mockups, or Mermaid/TikZ-looking output. Do not put the figure caption inside the image. The paper or document system should own captions and numbering.

Never start from image generation. Start from understanding the thesis, the implemented system, the source code, and the reviewer-facing argument. A correct boring diagram beats a beautiful false diagram.

## Workflow

1. Research the thesis topic, chapter structure, accepted reference theses, and school format rules.
2. Inspect the implemented system and code to extract real modules, entities, data flows, services, pages, storage, and user operations.
3. Convert the implementation into a thesis-friendly explanation model: requirements, overall design, detailed design, implementation, testing.
4. Audit existing figures and mark mock diagrams, Mermaid/TikZ figures, code-generated charts, modern architecture posters, oversized diagrams, and misplaced figures for replacement.
5. Choose the traditional diagram type expected in the target chapter.
6. Reduce the figure to stable textbook symbols and short Chinese labels.
7. Write a COSTAR image prompt with strict composition constraints.
8. Generate one figure at a time, preferably landscape if it contains many nodes.
9. Inspect for academic legibility: no cropped nodes, no crossing arrows, no decorative styling, no caption in the image.
10. Insert the image near the paragraph that first introduces it, then add a normal thesis caption outside the image.

For the full audit-and-upgrade workflow, load [references/research-audit-workflow.md](references/research-audit-workflow.md).

## Pre-Generation Research

Before writing prompts, gather enough evidence to avoid making decorative but inaccurate diagrams:

- Thesis structure: chapter titles, section goals, figure numbering, and chapter-summary style.
- Accepted examples: what diagrams appear in the same chapter of approved theses, especially adult-education or second-degree theses.
- System implementation: source-code directory tree, routes/pages, service modules, database schema, API contracts, storage objects, export/import flows, and test/demo paths.
- Paper narrative: how the author explains the system in old-school software-engineering language.
- Existing diagram inventory: figure filename, caption, source type, chapter location, and replacement decision.

Treat the source code as evidence, but translate it into thesis language. For example, a Next.js route becomes a "前端页面模块"; an API handler becomes a "业务处理模块"; object storage becomes a "文件存储"; an export endpoint becomes a "文档导出处理".

## Figure Audit and Replacement Rules

Replace or redesign figures when any of these are true:

- The figure is a mock placeholder that does not reflect the actual system.
- The figure is generated directly from Mermaid/TikZ/code and looks cramped, mechanical, colorful, or visually inconsistent with a thesis.
- The figure contains hover boxes, UI artifacts, code labels, markdown, internal captions, or accidental tool output.
- The diagram type is placed in the wrong chapter, such as ER diagrams in requirements analysis or deployment diagrams before overall design.
- The ER diagram is too shallow and only lists a few entities without attributes or cardinalities.
- The DFD is actually a modern service dependency graph and lacks external entities, processes, data stores, or data-flow direction.
- The flowchart exceeds the page, has crossing arrows, or lacks start/end and decision branch labels.

Do not "patch" bad diagrams by shrinking them. Rebuild the content model, split the figure if needed, then regenerate.

## Chapter Placement Rules

Use figures where an older computer-science thesis reviewer expects them.

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

When upgrading an existing thesis, first create a figure map:

| Existing figure | Current chapter | Problem | Replacement type | Target chapter |
| --- | --- | --- | --- | --- |
| mock architecture | requirements | wrong abstraction | context DFD | requirements |
| Mermaid ER | design | too simple | full ER + sub-ER | database design |
| TikZ data flow | design | cluttered/crossing arrows | traditional DFD | overall design |

## Traditional Style Requirements

Use these visual constraints unless the user gives a stricter school template:

- White background, black or dark-gray lines, no gradients, no shadows, no icons unless required by the diagram convention.
- Songti/SimSun-like Chinese labels if possible; English labels in Times-like serif if needed.
- Thin, consistent strokes; right-angle or straight arrows; no hover boxes, floating decorations, or canvas artifacts.
- Nodes arranged on a clear grid with generous spacing.
- Labels short enough to fit: usually 2-8 Chinese characters per node.
- Image should be high resolution and clean enough for A4 thesis insertion at single-column width.
- Do not include "图 x.x" or explanatory caption text inside the image.

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

## COSTAR Prompt Pattern

Use this pattern for each image-model request:

```text
Context: This figure is for a Chinese adult-education undergraduate computer-science thesis. It is based on the actual implemented system and source-code analysis. It must look like a traditional textbook diagram, not a modern product diagram.

Objective: Generate a high-resolution black-and-white [diagram type] for [chapter/section purpose].

Style: Conservative academic style, white background, thin black lines, simple geometric symbols, Songti-like Chinese labels, no color, no gradient, no shadow, no decorative icons, no caption inside the image.

Task: Draw the following nodes and relationships derived from the system analysis: [list nodes, relationships, arrows, cardinalities, branch labels].

Audience: Conservative undergraduate thesis reviewers who expect standard software-engineering diagrams.

Response: Output only the diagram image. Ensure all Chinese text is readable, no node is cropped, arrows do not cross boxes, layout fits A4 thesis insertion.
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
- Styling looks modern, colorful, promotional, or UI-dashboard-like.
- The figure is placed in a chapter where its diagram type does not belong.

For a stricter handoff checklist, load [references/review-checklist.md](references/review-checklist.md).

## Thesis Editing Notes

If replacing Mermaid/TikZ figures, remove the source diagram block from the thesis and insert the generated image asset. Keep the figure caption outside the image, using the thesis template's normal figure environment.

If replacing a code-generated figure, delete the brittle generation path from the final thesis source unless the project intentionally keeps reproducible figure generation. The submitted thesis should not reveal accidental implementation scaffolding.

If a generated diagram is too large, do not shrink it until unreadable. Split it into a main figure plus subfigures or move the oversized details to an appendix.

If the user says "最能让我毕业", prefer boring completeness over elegance: full DFD, full ER plus sub-ER, standard flowcharts, screenshots in implementation, and chapter-consistent placement.
