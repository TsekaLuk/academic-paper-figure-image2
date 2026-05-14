# Prompt Templates

Use these templates with an image-generation model. Replace bracketed fields before use.

## Context DFD

```text
Context: This figure is for a Chinese adult-education undergraduate computer-science thesis. It must look like a traditional software-engineering textbook data-flow diagram.

Objective: Generate a high-resolution black-and-white context data-flow diagram for the requirements analysis chapter of [system name].

Style: Conservative academic diagram, white background, thin black lines, no color, no gradient, no shadow. Use rectangles for external entities, one central circle or rounded process for the system, open-ended rectangles for data stores. Use Songti-like Chinese labels. No title or caption inside the image.

Task: Draw external entities [entity list]. Draw central process "[system process name]". Draw data stores [data store list]. Draw directed arrows with short labels: [data flows]. Keep arrows straight or right-angled and never crossing boxes.

Audience: Conservative undergraduate thesis reviewers who expect standard data-flow diagrams.

Response: Output only the diagram image. Ensure all Chinese text is readable, no node is cropped, layout fits A4 thesis insertion.
```

## Level-0 DFD

```text
Context: This figure is for a Chinese adult-education undergraduate computer-science thesis. It must look like a traditional structured-analysis data-flow diagram.

Objective: Generate a high-resolution black-and-white level-0 data-flow diagram for [system name].

Style: Traditional textbook DFD, white background, thin black lines, simple circles or rounded rectangles for processes, rectangles for external entities, open-ended rectangles for data stores, no decorative icons, no caption inside the image.

Task: Arrange processes from left to right: [P1 process], [P2 process], [P3 process], [P4 process]. External entities: [entities]. Data stores: [D1], [D2], [D3]. Draw arrows: [flow list]. Use short Chinese labels on arrows where useful. Keep a clean grid layout with ample spacing.

Audience: Adult-education computer-science thesis reviewers.

Response: Output only the diagram image. No Mermaid style, no TikZ style, no color.
```

## Traditional ER Diagram

```text
Context: This figure is for the database design section of a Chinese adult-education undergraduate computer-science thesis. It must use the traditional Chen ER style taught in software-engineering textbooks.

Objective: Generate a high-resolution black-and-white ER diagram for [system name].

Style: White background, rectangles for entities, diamonds for relationships, ovals for attributes, thin black lines, black Chinese labels in a Songti-like font, no colors, no gradients, no shadows, no title or caption inside the image.

Task: Draw these entities and attributes:
- [Entity 1]: [attributes]
- [Entity 2]: [attributes]
- [Entity 3]: [attributes]
- [Entity 4]: [attributes]

Draw these relationships with cardinalities near lines:
- [Entity A] [relationship] [Entity B], cardinality [1:N / M:N]
- [Entity C] [relationship] [Entity D], cardinality [1:1 / 1:N]

Keep attributes close to their entity, avoid overlap, and split into balanced left/right groups if needed.

Audience: Conservative undergraduate thesis reviewers who expect a complete, traditional ER diagram.

Response: Output only the diagram image. Ensure cardinalities and Chinese text are readable.
```

## ER Subgraph

```text
Context: This figure is for a Chinese adult-education undergraduate computer-science thesis. It supplements the overall ER diagram with a clearer entity relationship subgraph.

Objective: Generate a high-resolution black-and-white traditional ER subgraph for [module/entity cluster name].

Style: Chen ER notation, rectangles for entities, diamonds for relationships, ovals for attributes, thin black lines, white background, no colors, no title, no caption inside the image.

Task: Focus only on these entities: [entity list]. Include practical attributes: identifiers, names, status, timestamps, type fields, ownership fields, file paths, version numbers, or permission fields as applicable. Draw relationships and cardinalities: [relationships].

Audience: Undergraduate computer-science thesis reviewers checking whether the database design is sufficiently detailed.

Response: Output only the diagram image, readable at A4 thesis width.
```

## Business Flowchart

```text
Context: This figure is for the requirements analysis chapter of a Chinese adult-education undergraduate computer-science thesis. It should look like a standard textbook business process flowchart.

Objective: Generate a high-resolution black-and-white business flowchart for [business scenario].

Style: White background, terminal ovals for start/end, process rectangles, decision diamonds, document symbols if needed, thin black arrows, Songti-like Chinese labels, no decorative icons, no caption inside the image.

Task: Draw the process in order:
1. 开始
2. [process step]
3. [process step]
4. decision diamond: [question]
5. branch 是 -> [step]
6. branch 否 -> [step]
7. 结束

Use horizontal or vertical layout, not diagonal spaghetti. Label decision branches with 是 and 否.

Audience: Conservative thesis reviewers.

Response: Output only the diagram image, no title, no caption, no watermark.
```

## Functional Module Diagram

```text
Context: This figure is for the overall design chapter of a Chinese adult-education undergraduate computer-science thesis. It must look like a traditional hierarchical module structure diagram.

Objective: Generate a high-resolution black-and-white functional module diagram for [system name].

Style: White background, thin black rectangular boxes, hierarchical tree layout, no icons, no color, no gradient, no caption inside the image.

Task: Top node: [system name]. Second-level modules: [module list]. Third-level functions under each module: [function list grouped by module]. Use vertical connector lines and horizontal distribution. Keep all labels short and readable.

Audience: Adult-education computer-science thesis reviewers.

Response: Output only the diagram image. Ensure it fits one A4 page width.
```

## Conservative Architecture Diagram

```text
Context: This figure is for the overall design chapter of a Chinese adult-education undergraduate computer-science thesis. It should look like a simple layered architecture diagram from a software-engineering textbook.

Objective: Generate a high-resolution black-and-white system architecture diagram for [system name].

Style: Traditional academic architecture diagram, white background, rectangular layers, thin black lines, no cloud marketing icons, no colorful product style, no caption inside the image.

Task: Draw layers from top to bottom or left to right:
- 用户层: [clients]
- 表现层: [front-end pages]
- 业务层: [services/modules]
- 数据层: [database/file storage/cache]
- 外部服务: [optional services]

Draw arrows only for main dependencies. Avoid crossing arrows and avoid diagonal lines unless unavoidable.

Audience: Conservative undergraduate thesis reviewers.

Response: Output only the diagram image with readable Chinese labels.
```
