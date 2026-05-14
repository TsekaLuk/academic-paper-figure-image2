# Research and Audit Workflow

Use this workflow when upgrading thesis figures from mock, Mermaid, TikZ, code-generated, or visually poor diagrams into image-model-generated academic figures.

## 1. Build Thesis Context First

Read the thesis before designing figures:

- record chapter titles and section purposes;
- identify where figures are currently referenced;
- inspect accepted sample theses from the same school or teacher;
- note school-specific requirements for captions, fonts, page width, and figure placement;
- identify whether "需求分析" and "总体设计" are separated, because figure placement depends on this boundary.

Expected outcome: a chapter-to-figure map, not image prompts yet.

## 2. Understand the Real System

Inspect source code and artifacts. Extract thesis-level concepts:

| Code artifact | Thesis concept |
| --- | --- |
| route/page/component | 页面模块 / 交互模块 |
| API route/controller | 业务处理模块 |
| database table/model | 实体 / 数据表 |
| object storage/upload folder | 文件存储 |
| export or render endpoint | 文档生成 / 导出模块 |
| auth/session/role logic | 用户权限模块 |
| test/demo script | 测试流程 / 应用场景 |

Do not paste code into the figure or paper正文. Convert code into old-school software-engineering terms.

## 3. Build the Paper Logic

Before drawing, decide what each chapter is proving:

- Requirements analysis proves the system is needed and the functional boundary is clear.
- Overall design proves the system has modules, architecture, data flow, and storage design.
- Detailed design proves key processes and database relationships are sufficiently concrete.
- Implementation proves the system exists through interface screenshots and module operation flows.
- Testing proves the system can complete the expected scenarios.

Every figure should support one of these proof goals.

## 4. Audit Existing Figures

Create a replacement table:

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

## 5. Choose Replacement Figure Types

Use this default mapping:

| Problem | Replacement |
| --- | --- |
| vague system explanation | context DFD or business flowchart |
| missing requirements proof | use-case diagram + level-0 DFD |
| weak overall design | architecture diagram + module hierarchy |
| data flow unclear | traditional DFD with stores and arrows |
| database design too thin | full ER + 2-4 sub-ER figures |
| implementation looks abstract | UI screenshots + operation flowcharts |
| testing lacks evidence | test scenario flow + test case table |

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
