# Q563 appendix: exponentially accurate high-confidence expansion for an unequal split

Fix dimension d, and fixed sizes M>m≥1. Write L=log(1/α), let u,v be the larger- and smaller-split means, and set D=||u−v||. With the likelihood ratio formula of the delivered proof, the larger-split term is exp(M(||θ−u||²−D²)/2), and the smaller term uses m and v. The region consists of points where the sum is below 2e^L.

It lies in the ball about u with radius R, R²=D²+2(L+log 2)/M. On E_L={D≤η√L}, every point in that ball has distance at most R+D from v, so the smaller-split log term is at most (m/2)(R+D)². Dividing by L, a uniform upper bound is (m/2)(√(η²+2(1+log 2/L)/M)+η)². Choose η>0 sufficiently small that the limiting quantity is <1, since at η=0 the limit is m/M<1. Then choose any ρ between that limiting quantity and 1, and take L sufficiently large. The smaller term is at most e^{ρL} throughout the outer ball on E_L.

Put b_L=−log(1−e^{−(1−ρ)L}/2)=O(e^{−(1−ρ)L}). On E_L the open ball about u with squared radius R²−2b_L/M is contained in the confidence set: the larger term there is strictly less than 2e^L−e^{ρL}. Its diameter squared is 4R²−8b_L/M, while the outer upper bound is 4R². No direction or symmetry of the actual region is needed for this sandwich. Outside E_L use the nonnegative diameter and the same outer bound.

D² has law (1/M+1/m)χ²_d. Choose any a>0 strictly below the radius of convergence of its moment-generating function. Then E[(L+D²)1_{D²>η²L}] ≤ e^{−aη²L}[L E exp(aD²)+E D² exp(aD²)] = O(e^{−c'L}) for any c'<aη². Combining the two events gives, for some c>0 depending on the fixed sizes and dimension,

  E diam² = 8(L+log 2)/M + 4d(1/M+1/m) + O(e^{−cL}).

The error from replacing the diameter squared by 4R² is nonpositive. The expansion need not be uniform in dimension or a vanishing fractional split difference, and does not assert any optimum at moderate α. For the distinct balanced case use the separate d≥2 identity in the main proof; the argument here specifically requires m/M<1.

[Source for the two-fold statistic](https://arxiv.org/html/2104.14676v3#S4).
