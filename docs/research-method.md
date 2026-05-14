# Research Method

This repo treats thesis figures as research evidence, not decoration.

## Evidence Chain

```text
source code / thesis text / accepted samples / reviewer comments
        ↓
system model and chapter role
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
- Is it derived from the actual system or from generic imagination?
- Does it use the right old-school notation?
- Would it remain readable after insertion into an A4 thesis page?
- Does the nearby paragraph explain the figure in a conventional academic tone?

## Research Standard

The figure should be traceable back to system evidence:

| Evidence | Diagram output |
| --- | --- |
| users and roles | use-case diagram / business flowchart |
| module boundaries | functional module diagram |
| database schema | ER diagram and entity subgraphs |
| service interaction | data-flow diagram / process diagram |
| implementation path | operation flowchart / screenshot |
| test scenarios | test process diagram / result table |

The output is intentionally conservative. Novel visual language increases review risk.
