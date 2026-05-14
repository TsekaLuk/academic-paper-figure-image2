# Review Checklist

Use this checklist before inserting generated figures into a thesis.

## Figure Content

- The figure supports the paragraph immediately before or after it.
- The figure type matches the chapter: requirements use process/use-case/DFD; design uses architecture/module/ER; implementation uses flow/screenshots; testing uses test flow/results.
- The paper has no major prose-only design section where a conventional本科论文 would normally require a diagram.
- The image contains no internal caption, no "Figure", no watermark, no prompt residue, no Mermaid text, and no code.
- Every node label is short, readable, and in Chinese unless the term is a standard English technical term.
- All arrows have a clear direction and do not pass through boxes or text.

## Missing Figure Audit

- Requirements analysis has visual evidence for actors, business process, or data boundaries.
- Overall design has visual evidence for architecture, modules, and major data flow.
- Database design has ER evidence, not only table prose.
- Implementation has screenshots or process flowcharts for core user operations.
- Testing has test tables plus at least one process/scenario/result visual when the thesis length and system scope justify it.
- Added figures are not filler: each one answers a likely reviewer complaint.

## Data Flow Diagram

- External entities are visually distinct from processes.
- Processes are numbered or clearly named if there are multiple processes.
- Data stores are shown and named as `D1`, `D2`, etc. when appropriate.
- Data flow direction is visible and not implied by layout alone.
- The diagram is not a modern service-dependency diagram pretending to be a DFD.

## ER Diagram

- Entities, attributes, and relationships use traditional ER notation.
- Relationship diamonds contain verbs such as `创建`, `拥有`, `生成`, `属于`, `提交`, `关联`.
- Cardinalities are present: `1`, `N`, `1:N`, `M:N`.
- The database design looks complete enough for an undergraduate system: users, documents, versions, tasks, export files, permissions/logs as applicable.
- If the overall diagram is crowded, use sub-ER figures instead of shrinking all text.

## Flowchart

- Start and end nodes exist.
- Decision nodes are diamonds and branches are labeled `是` / `否`.
- The process direction is consistent, usually top-to-bottom or left-to-right.
- Long flows are split into subprocess diagrams.

## Visual Style

- Structural diagrams such as DFD, ER, module, architecture, flowchart, and sequence diagrams are black-and-white or grayscale by default.
- Data visualizations may use restrained academic color when it improves comparison or readability.
- Color charts must remain print-safe: use direct labels, line styles, markers, hatching, or a clear legend so the result still works in grayscale copies.
- No shadows, gradients, rounded modern cards, glowing lines, product icons, decorative backgrounds, dashboard styling, or colorful swimlanes.
- Reject rainbow palettes, neon colors, color-only encodings, and any chart whose values cannot be traced to thesis evidence.
- Line weight is consistent.
- White space is sufficient; nothing touches image borders.
- It remains readable after insertion into an A4 page at normal thesis width.

## Placement

- Figure is placed after first mention, not before the section explains it.
- Figure number and caption are handled by the thesis template, outside the image.
- No figure floats into an unrelated chapter/section.
- Oversized detail diagrams are moved to appendix only when the main text has a smaller summary figure.
