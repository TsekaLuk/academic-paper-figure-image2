# Research and Audit Workflow

Use this workflow when upgrading thesis figures from mock, Mermaid, TikZ, code-generated, or visually poor diagrams into image-model-generated academic figures, and when adding missing diagrams/tables that a本科论文 should have but currently hides behind prose.

## 1. Build Thesis Context First

Read the thesis before designing figures:

- record chapter titles and section purposes;
- classify the thesis type: software system, mathematical modeling, data analysis, market research, management case, education research, finance/accounting, or hybrid;
- identify where figures are currently referenced;
- inspect accepted sample theses from the same school or teacher;
- note school-specific requirements for captions, fonts, page width, and figure placement;
- identify whether "需求分析" and "总体设计" are separated, because figure placement depends on this boundary.

Expected outcome: a chapter-to-figure map, a missing-figure map, and a domain-material checklist, not image prompts yet.

## 2. Understand the Real Evidence

For software theses, inspect source code and artifacts. For non-software theses, inspect data, formulas, questionnaires, interview outlines, case evidence, financial statements, statistical outputs, and result tables.

Extract thesis-level concepts:

| Code artifact | Thesis concept |
| --- | --- |
| route/page/component | 页面模块 / 交互模块 |
| API route/controller | 业务处理模块 |
| database table/model | 实体 / 数据表 |
| object storage/upload folder | 文件存储 |
| export or render endpoint | 文档生成 / 导出模块 |
| auth/session/role logic | 用户权限模块 |
| test/demo script | 测试流程 / 应用场景 |
| formula group | 模型建立 / 求解过程 |
| survey sheet | 样本统计 / 问卷维度 |
| data spreadsheet | 数据来源 / 变量说明 / 预处理 |
| financial statement | 指标体系 / 趋势分析 |
| case material | 问题诊断 / 原因分析 / 对策设计 |

Do not paste raw code, raw spreadsheet dumps, or raw statistical output into the figure or paper正文. Convert evidence into field-appropriate academic figures or tables.

## 3. Build the Paper Logic

Before drawing, decide what each chapter is proving. For software theses:

- Requirements analysis proves the system is needed and the functional boundary is clear.
- Overall design proves the system has modules, architecture, data flow, and storage design.
- Detailed design proves key processes and database relationships are sufficiently concrete.
- Implementation proves the system exists through interface screenshots and module operation flows.
- Testing proves the system can complete the expected scenarios.

Every figure should support one of these proof goals.

For other fields, use the same logic but change the proof target:

- Mathematical modeling proves assumptions, variables, model construction, solving process, and validation.
- Data analysis proves data source, preprocessing, statistical pattern, model result, and interpretation.
- Market research proves questionnaire design, sample credibility, analysis results, and recommendation basis.
- Management case proves problem identification, cause analysis, countermeasure design, and implementation feasibility.
- Finance/accounting proves data source, indicator system, trend/comparison, risk diagnosis, and suggestions.

## 4. Audit Existing Figures and Missing Figures

Create a replacement table for bad existing figures:

| Figure | Source type | Current problem | Decision |
| --- | --- | --- | --- |
| architecture figure | Mermaid/TikZ/mock/image | wrong chapter, cluttered, too modern, inaccurate, too simple | keep / redraw / split / move / delete |

Common replacement decisions:

- Replace Mermaid/TikZ when the geometry looks cramped, arrows cross, text overlaps, or it exposes tool-like aesthetics.
- Replace mock diagrams when labels are generic and not backed by actual system modules.
- Replace code-generated diagrams when they look like debugging output instead of thesis figures.
- Split large ER diagrams into an overall ER plus entity subgraphs.
- Move oversized grammar/code diagrams to appendix.
- Delete meaningless scenario diagrams that do not add design or test evidence.

Then create a missing-figure table for prose-only sections:

| Section | Current prose claim | Expected本科图 | Risk if absent | Decision |
| --- | --- | --- | --- | --- |
| 需求分析 | describes users and operations | 用例图 / 业务流程图 / 顶层DFD | reviewer says requirements are empty prose | add figure |
| 总体设计 | describes modules and architecture | 系统架构图 / 功能模块图 / 数据流图 | reviewer says design is not visualized | add figure |
| 数据库设计 | lists tables only | 总体ER图 / 局部ER图 | reviewer says database design is too simple | add figure |
| 系统实现 | describes operation process | 关键流程图 / 系统截图 | reviewer says no implementation evidence | add figure |
| 系统测试 | lists test cases only | 测试流程图 / 场景流程图 | reviewer says testing lacks process proof | add figure |

Missing figures are not optional decoration. In conservative undergraduate theses, they often function as proof that the author performed requirements analysis, system design, database design, implementation, and testing.

## 5. Choose Replacement Figure Types

Use this default software mapping:

| Problem | Replacement |
| --- | --- |
| vague system explanation | context DFD or business flowchart |
| missing requirements proof | use-case diagram + level-0 DFD |
| weak overall design | architecture diagram + module hierarchy |
| data flow unclear | traditional DFD with stores and arrows |
| database design too thin | full ER + 2-4 sub-ER figures |
| implementation looks abstract | UI screenshots + operation flowcharts |
| testing lacks evidence | test scenario flow + test case table |
| long prose but no figure | add the expected textbook figure for that chapter |

Use this minimum coverage heuristic for system-design theses:

| Chapter | Minimum visual evidence |
| --- | --- |
| 需求分析 | 用例图 or 业务流程图, and DFD when data movement is central |
| 总体设计 | 架构图, 功能模块图, 数据流图 |
| 数据库/详细设计 | 总体ER图 plus局部ER图 when entities exceed 5-6 |
| 系统实现 | screenshots plus key operation flowcharts |
| 系统测试 | test case table plus test process/scenario figure |

For non-software theses, load [cross-domain-figure-playbook.md](cross-domain-figure-playbook.md) and build an equivalent field-specific minimum coverage table before prompting image generation.

## 6. Generate With Evidence-Based Prompts

Each image prompt should include:

- where the figure will be inserted;
- what source-code/system evidence it represents;
- exact nodes and relationships;
- traditional notation rules;
- no internal caption;
- no modern style;
- readability and A4 insertion constraints.

Generate one figure at a time. Large batch prompts increase the risk of inconsistent notation and garbled Chinese.

## 7. Insert and Verify

After inserting:

- compile or export the paper;
- inspect the actual PDF/Word page, not only the raw image;
- verify that the caption is outside the image;
- check that the text remains readable at final size;
- check that the figure appears after the first textual reference;
- update nearby paragraphs so the figure is introduced in a conventional thesis tone.

If a reviewer may say "图乱放", the figure is not done even if the image itself is high quality.
