# Prompt Templates

Use these templates with an image-generation model. Replace bracketed fields before use.

For non-software domains, use the generic cross-domain template in [cross-domain-figure-playbook.md](cross-domain-figure-playbook.md) first, then specialize it with the templates below.

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

## Mathematical Modeling Flow

```text
Context: This figure is for a Chinese undergraduate mathematical-modeling thesis. It must look like a conservative textbook-style model-building flowchart.

Objective: Generate a high-resolution black-and-white model construction and solution flowchart for [problem name].

Style: White background, thin black lines, terminal ovals for start/end, rectangles for process steps, diamonds for key judgments, Songti-like Chinese labels, no color, no gradient, no shadow, no caption inside the image.

Task: Draw the flow from top to bottom: 问题分析 -> 基本假设 -> 符号定义 -> 模型建立 -> 参数估计 -> 模型求解 -> 结果检验 -> 灵敏度分析 -> 结论输出. Replace or extend these nodes with the thesis-specific steps: [specific steps]. Keep each node label short.

Audience: Conservative undergraduate reviewers who expect standard mathematical-modeling visual materials.

Response: Output only the diagram image. Ensure labels are readable and no node is cropped.
```

## Data Analysis Process

```text
Context: This figure is for a Chinese undergraduate data-analysis thesis. It must show the data processing and analysis process in a traditional academic style.

Objective: Generate a high-resolution black-and-white data analysis flowchart for [topic].

Style: White background, thin black process boxes and arrows, conservative academic layout, Songti-like Chinese labels, no dashboard style, no color, no caption inside the image.

Task: Draw the process: 数据来源 -> 数据清洗 -> 缺失值处理 -> 描述性统计 -> 特征分析 -> 模型建立 -> 结果评价 -> 结论解释. Use these thesis-specific variables or data sources: [data/source/variables]. Avoid decorative icons.

Audience: Undergraduate thesis reviewers checking whether data analysis is standardized.

Response: Output only the diagram image, readable at A4 thesis width.
```

## Data Visualization Chart

```text
Context: This chart is for a Chinese undergraduate thesis in [field]. It is based on verified thesis evidence: [dataset/experiment output/questionnaire result/statistical table/financial statement/model result]. It must look like a conservative academic chart, not a dashboard or colorful infographic.

Objective: Generate a high-resolution [bar chart/line chart/scatter plot/heatmap/distribution chart/model-comparison chart] for [chapter/section purpose].

Style: White background, clean axes, readable Songti-like Chinese labels, Times-like numbers, restrained print-safe academic colors only if they improve comparison, no gradient, no shadow, no decorative icons, no 3D effect, no internal caption or figure number.

Task: Plot these exact values or relationships: [series/categories/periods/metrics/units]. Use a clear legend or direct labels. Use line styles, markers, hatching, or annotations so the chart remains understandable in grayscale printing.

Audience: Conservative undergraduate thesis reviewers who expect traceable data evidence and readable academic charts.

Response: Output only the chart image. Do not invent values. Do not include a title, watermark, caption, or explanatory paragraph inside the image.
```

## Market Research Structure

```text
Context: This figure is for a Chinese undergraduate market-research thesis. It must look like a conservative questionnaire-analysis diagram or table-style figure.

Objective: Generate a high-resolution black-and-white questionnaire structure and analysis framework figure for [research topic].

Style: White background, thin black rectangular boxes, clear table-like or hierarchy layout, Songti-like Chinese labels, no colorful infographic style, no caption inside the image.

Task: Show these survey dimensions: [dimension list]. Under each dimension, show representative indicators: [indicator list]. Add an analysis path from 问卷设计 -> 样本收集 -> 信度效度检验 -> 描述统计 -> 交叉分析 -> 问题诊断 -> 对策建议.

Audience: Conservative undergraduate thesis reviewers who expect questionnaire design and analysis evidence.

Response: Output only the figure image, no title or watermark.
```

## Management Diagnosis Diagram

```text
Context: This figure is for a Chinese undergraduate management or business-case thesis. It must use a conservative textbook-style problem diagnosis diagram.

Objective: Generate a high-resolution black-and-white [fishbone/SWOT/PEST/process] diagram for [case/company/problem].

Style: White background, thin black lines, simple geometric shapes, Songti-like Chinese labels, no color, no gradient, no decorative business icons, no caption inside the image.

Task: Represent the central problem as [problem]. Use these cause or factor groups: [groups]. Include these case-specific factors: [factors]. Keep the layout balanced and readable.

Audience: Conservative undergraduate reviewers expecting a standard management-analysis framework.

Response: Output only the diagram image.
```

## Finance Indicator Analysis

```text
Context: This figure is for a Chinese undergraduate finance or accounting thesis. It must look like a conservative academic indicator-analysis chart or framework.

Objective: Generate a high-resolution [indicator-system/trend/comparison/DuPont] figure for [company/topic].

Style: White background, restrained academic table/chart style, Songti-like Chinese labels, no dashboard style, no decorative icons, no caption inside the image. For trend or comparison charts, restrained print-safe academic color is acceptable when it improves distinction; also use labels, markers, line styles, or hatching so the chart remains readable in grayscale.

Task: Use these indicators: [indicator list]. Use these periods or comparison objects: [periods/peers]. Show the analysis structure from 数据来源 -> 指标计算 -> 趋势分析 -> 同行比较 -> 问题诊断 -> 改进建议.

Audience: Conservative undergraduate finance/accounting thesis reviewers.

Response: Output only the figure image.
```
