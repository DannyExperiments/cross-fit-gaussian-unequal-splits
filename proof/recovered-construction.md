# Balanced cross-fit Gaussian splitting need not minimize expected squared diameter

Let a=n₀, b=n₁, M=max(a,b), m_j=Ȳ_j, D=||m₀−m₁|| and ℓ=log(1/α)>0. The likelihood ratio for testing on partition j and using the opposite mean in the numerator is exp(n_j(||θ−m_j||²−D²)/2), by completing the square in the Gaussian log-likelihood. Therefore the average of the two exponentials must be below exp(ℓ). If both are below exp(ℓ), the average qualifies; if the average qualifies, each is below 2 exp(ℓ). Writing B(c,r) for the open ball, this gives
intersection_j B(m_j,√(D²+2ℓ/n_j)) ⊆ C_CF ⊆ intersection_j B(m_j,√(D²+2(ℓ+log 2)/n_j)).

Put s=√(2ℓ/M). The inner intersection contains the open ball about the midpoint of radius √(D²+s²)−D/2, by the triangle inequality. The outer intersection is contained in the ball corresponding to the larger sample. Consequently
8ℓ/M−4Ds ≤ diam(C_CF)² ≤ 4D²+8(ℓ+log 2)/M.
For the lower bound, if D≥s the displayed lower bound is nonpositive; otherwise the inner radius is at least s−D/2>0, and squaring twice that radius gives 4s²−4Ds+D². Open versus closed balls do not affect diameter suprema.

## Explicit counterexample

Take n=4, d=1, α=exp(−36). The distribution of m₀−m₁ is N_d(0,(1/a+1/b)I_d). Thus E D²=d(1/a+1/b), E D≤√(E D²). For the (2,2) split, E D≤1 and the lower bound is 144−24=120. For the (1,3) split, E D²=4/3 and the upper bound is 96+16/3+(8/3)log 2<104, since log 2<1. The unequal split is strictly better. This is a deterministic expectation certificate, not simulation.

## Further exact statements

For any fixed n,d and split, divide the displayed bounds by ℓ and let ℓ→∞; E D and E D² are finite constants. The limiting slope is 8/M. As there are only finitely many integer splits, (1,n−1) and its reflection uniquely minimize up to that symmetry for sufficiently small α whenever n≥4 is fixed. Nothing here says those splits are optimal at conventional confidence levels.

For balanced split a=b=h and d≥2, at midpoint coordinates z the average ratio is exp(h(||z||²−3D²/4)/2) cosh(h z·(m₁−m₀)/2). Since cosh≥1, the greatest possible norm is bounded by √(2ℓ/h+3D²/4), and approaching this norm along a direction perpendicular to m₁−m₀ gives opposite points in the set. Thus diam²=8ℓ/h+3D² exactly. For n=4,d=2,ℓ=36, the balanced expectation is 150, whereas the unequal upper bound is < 328/3 (less than 110).

Source: [Dunn–Ramdas–Balakrishnan–Wasserman, §3.1](https://arxiv.org/html/2104.14676#S3.SS1), [Dunn dissertation, Appendix B.3](https://robinmdunn.github.io/files/RobinDunn-dissertation.pdf#page=145). The conjecture concerns this cross-fit set, not single-split radius or volume. The known simulations do not address all α. No priority claim.
