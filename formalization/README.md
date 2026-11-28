# The univariate inner interval

For rational midpoint coordinates and nonnegative fold separation D, every point strictly between −(s−D/2) and s−D/2 belongs to both inner balls of squared radius D²+s². Every smaller nonnegative radius provides two antipodal witnesses.

The certificate covers the deterministic inner-interval step in dimension one. The likelihood-ratio reduction, real supremum, Gaussian expectations and optimal-split conclusions remain in the manuscript.

[Lean source](Q563Interval.lean) · [Mathematical source](../paper/manuscript.tex) · [Expected axiom report](expected-axioms.txt)

Replay from this directory with Lean 4.30.0 and its standard library.

```sh
lean -DwarningAsError=true Q563Interval.lean > axioms.actual
diff -u expected-axioms.txt axioms.actual
```
