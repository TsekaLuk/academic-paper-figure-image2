# Research Method

This repo treats thesis figures as research evidence, not decoration.

## Evidence Chain

```text
source code / data / formulas / questionnaires / case materials / thesis text / accepted samples / reviewer comments
        ↓
domain model and chapter role
        ↓
figure risk classification
        ↓
traditional diagram specification
        ↓
image2 generation prompt
        ↓
rendered PDF/Word inspection
```

## Audit Questions

- What claim does this figure prove?
- Is the figure in the chapter where a conservative thesis reviewer expects it?
- Is it derived from actual system/data/model/survey/case evidence or from generic imagination?
- Does it use the right old-school notation for the declared field?
- Would it remain readable after insertion into an A4 thesis page?
- Does the nearby paragraph explain the figure in a conventional academic tone?

## Research Standard

The figure should be traceable back to thesis evidence:

| Evidence | Diagram output |
| --- | --- |
| users and roles | use-case diagram / business flowchart |
| module boundaries | functional module diagram |
| database schema | ER diagram and entity subgraphs |
| service interaction | data-flow diagram / process diagram |
| implementation path | operation flowchart / screenshot |
| test scenarios | test process diagram / result table |
| model variables | symbol table / model-building flow |
| survey sample | sample profile / reliability-validity table |
| data spreadsheet | data dictionary / cleaning flow / statistics chart |
| finance statements | indicator table / trend chart / comparison table |
| case material | SWOT / PEST / fishbone / countermeasure matrix |

The output is intentionally conservative. Novel visual language increases review risk.
