# Claims and evidence

| Claim | Evidence |
| --- | --- |
| A 1–3 split beats a 2–2 split at n = 4, d = 1, α = exp(−36) | [Theorem 1](paper/manuscript.pdf) and [exact replay](verification/results/replay.txt) |
| The leading expected squared-diameter slope is 8/M | [Theorem 1](paper/manuscript.pdf) |
| The balanced squared diameter is exact in dimension at least two | [Proposition 2](paper/manuscript.pdf) |
| Fixed unequal splits have an exponentially accurate two-term expansion | [Proposition 3](paper/manuscript.pdf) and [supplement](proof/unequal-split-expansion.md) |
| The paper and dissertation pose this exact objective | [Primary sources and comparison](audits/public_safe_reports/LITERATURE.md) |

## Partial Lean verification

For rational midpoint coordinates and nonnegative fold separation D, every point strictly between −(s−D/2) and s−D/2 belongs to both inner balls of squared radius D²+s². Every smaller nonnegative radius provides two antipodal witnesses. [Scope, source and replay](formalization/README.md)
