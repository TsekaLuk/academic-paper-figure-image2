<p align="center">
  <img src="./assets/social-card.png" alt="Academic Paper Figure Image2" width="920">
</p>

<p align="center">
  <a href="./README.md"><img src="https://img.shields.io/badge/lang-English-lightgrey?style=flat-square" alt="English"></a>
  <a href="./README.zh-CN.md"><img src="https://img.shields.io/badge/lang-%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-black?style=flat-square" alt="简体中文"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/%E7%B1%BB%E5%9E%8B-Agent%20Skill-black?style=flat-square" alt="Agent Skill">
  <img src="https://img.shields.io/badge/%E9%80%82%E7%94%A8-%E4%B8%AD%E6%96%87%E6%9C%AC%E7%A7%91%E8%AE%BA%E6%96%87-555?style=flat-square" alt="适用范围">
  <img src="https://img.shields.io/badge/%E6%96%B9%E6%B3%95-%E7%A0%94%E7%A9%B6%E4%BC%98%E5%85%88-555?style=flat-square" alt="研究优先">
  <a href="https://github.com/TsekaLuk/academic-paper-figure-image2/stargazers"><img src="https://img.shields.io/github/stars/TsekaLuk/academic-paper-figure-image2?style=flat-square&label=star&color=black" alt="Stars"></a>
</p>

# 学术论文配图 Image2

> **你的系统也许够用了——真正让你被打回的，是图和它们的位置。**
> 面向保守本科论文配图的「研究优先」图像生成工作流。

这个 skill 把杂乱、缺失或评委不待见的论文配图，转化为传统、教科书风格的学术图。覆盖软件类图、数学建模流程图、数据分析图表、市场调研问卷可视化、管理诊断图、教育研究证据图，以及财务/会计指标图。

它针对的场景是：论文不是因为没做工作而被打回，而是因为该领域应有的图料缺失、放错章节、画得粗糙、像 Mermaid/TikZ/开发风、或与保守本科论文审美不一致。

> English readers, take the portal → **[English README](./README.md)**

## 它优化什么

- **可过性：** 配图符合所声明专业里老派本科论文的预期。
- **专业贴合：** 配图贴合论文专业，而不是把每篇论文都硬塞成软件类图。
- **证据性：** 配图来自论文论点、源代码、数据、公式、问卷、案例材料、财务报表、截图与测试流程。
- **位置：** 每张图归属正确章节，并出现在它支撑的那一段附近。
- **视觉克制：** 教科书化、可打印；结构类图默认黑白，数据可视化在能改善对比时可用克制的学术配色。
- **替换纪律：** mock、Mermaid、TikZ、代码生成、拥挤或装饰性的图，一律审查并升级。

## 核心工作流

```text
论文 + 代码 + 已通过样本
        ↓
配图清单 + 缺图审计
        ↓
贴合章节的图规划
        ↓
COSTAR image2 提示词
        ↓
生成的学术配图
        ↓
PDF / Word 成稿页检查
```

## 使用场景

| 情况 | Skill 的处理 |
| --- | --- |
| ER 图过于简单 | 扩展为总体 ER 加子 ER 图 |
| Mermaid/TikZ 输出显得拥挤 | 替换为高分辨率、保守的学术图 |
| 需求章节只有文字 | 补用例图/业务流程图/上下文 DFD |
| 总体设计缺乏视觉佐证 | 补架构图/模块图/数据流图 |
| 数学建模部分只有公式 | 补符号表、建模流程、验证/灵敏度可视化 |
| 数据分析部分只有文字结论 | 补清洗流程、描述统计、相关性/模型评估图表 |
| 市场调研论文缺问卷证据 | 补问卷结构、样本画像、信效度、交叉表可视化 |
| 管理案例直接跳到对策 | 补 SWOT/PEST/鱼骨/流程/对策可视化 |
| 实现章节显得抽象 | 补系统截图与操作流程图 |
| 图放错了章节 | 按它在论文中的角色移动或重画 |

## 仓库地图

- [SKILL.md](./SKILL.md)：核心 agent 指令。
- [scripts/audit_figure_assets.py](./scripts/audit_figure_assets.py)：可复用的图片资产清单、SVG 字体风险审计和 contact sheet 生成脚本。
- [references/research-audit-workflow.md](./references/research-audit-workflow.md)：论文/代码/配图审计工作流。
- [references/cross-domain-figure-playbook.md](./references/cross-domain-figure-playbook.md)：跨专业配图与材料 playbook。
- [references/prompt-templates.md](./references/prompt-templates.md)：可复用的 image2 提示词模板。
- [references/review-checklist.md](./references/review-checklist.md)：配图终审清单。
- [docs/research-method.md](./docs/research-method.md)：研究质量框架。
- [docs/growth-playbook.md](./docs/growth-playbook.md)：增长黑客式封装逻辑。
- [assets/image2-prompts.md](./assets/image2-prompts.md)：仓库品牌视觉素材提示词。

## 图像生成说明

在暴露了内置图像生成工具的 Codex 会话里，直接使用该工具来产出一次性的仓库美术图与论文配图素材。不要错误地以为本地 `imagegen` CLI 是唯一路径。

只有在确实需要可复现的批量生成、脚本化运行或本地 API 参数控制时，才使用本地 CLI。此时 CLI 可能需要 `OPENAI_API_KEY`。

## 字体安全与工具链

如果现有 image2 图的结构已经正确，只是字体不合规，应当用图像模型对原图做端到端字体编辑，不要为了换字体把它改成 Python/Pillow/Matplotlib 重画图。对江苏海洋大学风格的正文图表，默认要求是：图内中文五号 `KaiTi_GB2312`，英文、数字、模型名和公式五号 `Times New Roman` 或同等学术衬线字体；图题和编号交给论文模板，不写进图片。

每次大规模替换前先跑资产审计：

```bash
python scripts/audit_figure_assets.py thesis/figures/generated \
  --recursive \
  --out-md /tmp/figure-audit.md \
  --contact-sheet /tmp/figure-contact-sheet.png
```

这个脚本会生成图片清单、尺寸、长宽比风险、SVG 字体风险和接触表。稳妥流程是：先备份原图，再区分 image2 图、代码图表和截图；image2 图用 Codex 内置生图/编辑工具处理，数据可视化回到源脚本修字体并重新渲染，最后重新编译 PDF/Word 并检查最终页，而不是只看单张图片。

## 增长定位

这个仓库封装了一个反复出现的「论文抢救」模式：

1. 评委的抱怨暴露出一条隐藏标准；
2. 隐藏标准变成一份审计清单；
3. 清单变成一个可复用的 skill；
4. 每一篇新论文都让提示词库和风险分类更强。

增长闭环不是「把图画得更漂亮」，而是「把评委的反对意见转化为可复用的验收标准」。

## 安装

如有 `.skill` 包则使用它，否则把本文件夹复制到你的 agent skills 目录：

```bash
cp -R academic-paper-figure-image2 ~/.agents/skills/
```

## 质量底线

一张生成的图，只有在准确、传统、在 A4 论文宽度下清晰可读、图内无标题、且放在正确章节时，才算合格。对于数据可视化，只有当配色克制、可打印、且有可追溯的论文数据支撑时，用色才可接受。

如果一张图看起来很唬人，但保守的本科论文评委会说一句「乱」，那它就是不合格。

---

<p align="center">
  如果它帮你省下了一轮论文返工，点个 ⭐ 能让更多同学找到它。<br>
  <sub><a href="./README.md">English</a> · <a href="./docs/growth-playbook.md">增长 Playbook</a> · <a href="./SKILL.md">SKILL.md</a></sub>
</p>
