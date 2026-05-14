# Review Checklist

Use this checklist before inserting generated figures into a thesis.

## Figure Content

- The figure supports the paragraph immediately before or after it.
- The figure type matches the chapter: requirements use process/use-case/DFD; design uses architecture/module/ER; implementation uses flow/screenshots; testing uses test flow/results.
- The image contains no internal caption, no "Figure", no watermark, no prompt residue, no Mermaid text, and no code.
- Every node label is short, readable, and in Chinese unless the term is a standard English technical term.
- All arrows have a clear direction and do not pass through boxes or text.

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

- Black-and-white or grayscale only.
- No shadows, gradients, rounded modern cards, glowing lines, product icons, or colorful swimlanes.
- Line weight is consistent.
- White space is sufficient; nothing touches image borders.
- It remains readable after insertion into an A4 page at normal thesis width.

## Placement

- Figure is placed after first mention, not before the section explains it.
- Figure number and caption are handled by the thesis template, outside the image.
- No figure floats into an unrelated chapter/section.
- Oversized detail diagrams are moved to appendix only when the main text has a smaller summary figure.
