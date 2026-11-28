import Std
namespace CrossFit
/-- The two common-radius inner balls in midpoint-centered coordinates. -/
def inner (d s z : Rat) : Prop :=
    (z+d/2)^2 < d^2+s^2 ∧ (z-d/2)^2 < d^2+s^2

theorem interior (d s z : Rat) (hd : 0 ≤ d) (lo : -(s-d/2) < z) (hi : z < s-d/2) :
    inner d s z := by
  have sq (x : Rat) (a : -s < x) (b : x < s) : x^2 < d^2+s^2 := by
    have := Rat.mul_pos (show 0 < s-x by grind) (show 0 < s+x by grind)
    have dd : 0 ≤ d*d := Rat.mul_nonneg hd hd
    grind
  exact ⟨sq _ (by grind) (by grind), sq _ (by grind) (by grind)⟩

/-- All radii below half the advertised inner diameter supply antipodal witnesses. -/
theorem antipodes (d s r : Rat) (hd : 0 ≤ d) (hr : 0 ≤ r) (h : r < s-d/2) :
    inner d s (-r) ∧ inner d s r ∧ r - (-r) = 2*r :=
  ⟨interior _ _ _ hd (by grind) (by grind), interior _ _ _ hd (by grind) (by grind), by grind⟩
#print axioms interior
#print axioms antipodes
end CrossFit
