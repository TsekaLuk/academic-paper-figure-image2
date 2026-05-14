# Cross-Domain Figure Playbook

Use this reference when the thesis is not a pure software-engineering design paper, or when the paper mixes software with modeling, survey, management, finance, education, or data-analysis materials.

The goal is not to decorate the thesis. The goal is to make the paper look like it belongs to its declared field and to remove the reviewer objection that "该有的图表没有".

## Universal Audit Pattern

1. Classify the thesis type before designing figures.
2. Read 2-3 accepted sample theses from the same field if available.
3. Build a material inventory: data, variables, samples, formulas, questionnaire items, interview outlines, indicators, cases, screenshots, tests.
4. Map each chapter to the conventional visual evidence for that field.
5. Add or replace figures only when they support a chapter role.
6. Generate conservative images with no internal caption, then insert captions through the thesis template.

## Domain Figure Matrix

| Field | Expected visual materials | Typical chapter placement | Common rejection risk |
| --- | --- | --- | --- |
| Software engineering / computer system | use-case diagram, DFD, module diagram, architecture diagram, ER diagram, flowchart, screenshots, test table | requirements, overall design, database design, implementation, testing | prose-only design, tiny ER, Mermaid/TikZ clutter, no screenshots |
| Mathematical modeling | problem-analysis diagram, assumption table, symbol table, model-building flowchart, solution flowchart, fitting/residual chart, sensitivity/error analysis chart | problem restatement, assumptions, model construction, solution, validation | formulas appear without variables/process, no validation or sensitivity proof |
| Data analysis / statistics | data-source table, data dictionary, cleaning flowchart, descriptive statistics table, distribution chart, correlation heatmap, model-comparison table, evaluation metrics chart | data source, preprocessing, exploratory analysis, modeling, results | results are narrated but not supported by statistics or charts |
| Market research / questionnaire | questionnaire structure table, sample profile chart/table, reliability/validity table, frequency table, crosstab, satisfaction chart, problem-diagnosis matrix | survey design, sample analysis, empirical analysis, recommendations | questionnaire looks casual, no sample structure, no reliability/validity evidence |
| Management / business case | PEST, SWOT, Porter five forces, fishbone diagram, business process diagram, issue-cause-countermeasure table, implementation safeguard matrix | case background, problem analysis, cause analysis, countermeasures | generic suggestions without diagnosis framework or implementation table |
| Education research | research-object table, questionnaire/interview outline, classroom/process observation chart, score/statistics table, coding table, strategy framework diagram | research design, data collection, results, teaching suggestions | experience-style narration without tool, sample, or result evidence |
| Finance / accounting | indicator-system table, ratio trend chart, peer-comparison table, DuPont analysis diagram, cash-flow/structure chart, risk-warning matrix | company/industry overview, financial analysis, problem diagnosis, countermeasures | only copied statements, no indicator system or trend/comparison evidence |

## Required-Material Heuristics

### Mathematical Modeling

Add figures or tables when:

- variables appear in formulas but there is no symbol table;
- the model-building process is described in prose only;
- results are listed without fitting, residual, error, or sensitivity checks;
- multiple models are compared but there is no comparison table.

Prefer:

- "模型建立流程图";
- "主要符号说明表";
- "模型求解流程图";
- "灵敏度分析图";
- "误差分析图".

Avoid:

- decorative flowcharts that do not correspond to actual equations;
- advanced-looking charts without data source or explanation;
- color-heavy scientific posters.

### Data Analysis

Add figures or tables when:

- the data source is unclear;
- cleaning rules are described but not shown;
- descriptive analysis is only prose;
- a model is used but metrics are missing.

Prefer:

- "数据处理流程图";
- "变量说明表";
- "描述性统计表";
- "相关性分析图";
- "模型评价指标表".

Avoid:

- dashboard-like visuals;
- chart dumps with no chapter role;
- unexplained machine-learning diagrams.

### Market Research

Add figures or tables when:

- questionnaire design is not visible;
- sample distribution is not shown;
- reliability/validity is absent despite survey claims;
- recommendations are not tied to analysis results.

Prefer:

- "问卷维度设计表";
- "样本基本情况统计表";
- "信度与效度检验表";
- "交叉分析表";
- "问题诊断与改进建议表".

Avoid:

- flashy infographics;
- unverifiable sample numbers;
- adding reliability/validity tables if the paper has no real questionnaire data.

### Management Case

Add figures or tables when:

- the paper jumps from background to suggestions;
- the cause analysis is vague;
- countermeasures are not operational.

Prefer:

- "SWOT分析图";
- "鱼骨图";
- "业务流程图";
- "问题-原因-对策表";
- "实施保障矩阵".

Avoid:

- using every framework at once;
- frameworks not connected to the case facts.

### Finance and Accounting

Add figures or tables when:

- statements or ratios are mentioned without trend tables;
- peer comparison is claimed but not visualized;
- risks are listed without indicator evidence.

Prefer:

- "财务指标体系表";
- "偿债/营运/盈利能力趋势图";
- "同行对比表";
- "杜邦分析图";
- "风险指标汇总表".

Avoid:

- invented financial numbers;
- decorative charts that cannot be traced to statements.

## Cross-Domain Prompt Pattern

```text
Context: This figure is for a Chinese undergraduate thesis in [field]. The figure must match conservative field conventions and look like a textbook-style academic figure, not a modern poster or dashboard.

Objective: Generate a high-resolution black-and-white [figure/table/chart type] for the [chapter/section] of the thesis.

Style: White background, thin black lines, conservative academic layout, Songti-like Chinese labels, no gradient, no shadow, no decorative icons, no internal caption or figure number.

Task: Use these exact materials from the thesis: [variables/data/sample/framework/nodes/relationships]. Arrange them as [layout constraints]. Keep labels short and readable at A4 thesis width.

Audience: Conservative undergraduate thesis reviewers in [field] who expect standard visual materials.

Response: Output only the figure image. Do not include a title, watermark, caption, or explanatory paragraph inside the image.
```

## Placement Rule

If a figure exists only because it looks professional, delete it. If a reviewer can point to a paragraph and ask "证据在哪里", add the expected field-specific figure or table immediately after that paragraph.
