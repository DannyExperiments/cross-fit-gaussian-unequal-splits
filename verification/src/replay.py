"""Exact tests for the Gaussian fold geometry and expectation certificate."""

from fractions import Fraction as F
from itertools import product


def sqnorm(vector):
    return sum(value**2 for value in vector)


def sub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def log_ratio_from_data(test_fold, opposite_mean, theta):
    return sum(sqnorm(sub(y, theta)) - sqnorm(sub(y, opposite_mean)) for y in test_fold) / 2


def mean(fold):
    return tuple(sum(column) / len(fold) for column in zip(*fold))


def check_likelihood_identity():
    observations = [(F(-2), F(0)), (F(1), F(-1)), (F(3), F(2)), (F(-1), F(1))]
    grid = tuple(map(F, ("-3/2", "-1", "0", "1/2", "2")))
    checked = 0
    for size in (1, 2, 3):
        fold_0, fold_1 = observations[:size], observations[size:]
        mean_0, mean_1 = mean(fold_0), mean(fold_1)
        distance_sq = sqnorm(sub(mean_0, mean_1))
        for theta in product(grid, repeat=2):
            for fold, own, opposite in ((fold_0, mean_0, mean_1), (fold_1, mean_1, mean_0)):
                formula = (sqnorm(sub(theta, own)) - distance_sq) * F(len(fold), 2)
                assert log_ratio_from_data(fold, opposite, theta) == formula
                checked += 1
    assert checked == 150
    print(f"{checked} exact fold likelihood identities")


def check_expectation_certificate():
    level = 36
    balanced_mean_distance_bound = F(1)
    balanced_variance = F(1, 2) + F(1, 2)
    assert balanced_mean_distance_bound**2 == balanced_variance
    s = 6
    assert s**2 == F(2 * level, 2)
    lower = F(8 * level, 2) - 4 * balanced_mean_distance_bound * s
    unequal_variance = F(1) + F(1, 3)
    larger = 3
    # Use log(2) < 1, which follows from the power series e > 1+1.
    upper = 4 * unequal_variance + F(8 * (level + 1), larger)
    assert (lower, upper) == (120, 104) and upper < lower

    balanced_dim2 = F(8 * level, 2) + 3 * 2 * balanced_variance
    unequal_dim2_bound = 4 * 2 * unequal_variance + F(8 * (level + 1), larger)
    assert (balanced_dim2, unequal_dim2_bound) == (150, F(328, 3))
    assert unequal_dim2_bound < balanced_dim2
    print("Exact expectation certificate: d=1 unequal < 104 and balanced >= 120")
    print("Exact expectation certificate: d=2 unequal < 328/3 and balanced = 150")


def check_balanced_geometry():
    checked = 0
    for h, distance, axial, transverse in product(range(1, 5), range(4), range(-2, 3), range(-2, 3)):
        z = (F(axial, 2), F(transverse, 2))
        c_0 = (-F(distance, 2), F(0))
        c_1 = (F(distance, 2), F(0))
        f_0 = F(h, 2) * (sqnorm(sub(z, c_0)) - distance**2)
        f_1 = F(h, 2) * (sqnorm(sub(z, c_1)) - distance**2)
        center = F(h, 2) * (sqnorm(z) - F(3, 4) * distance**2)
        interaction = F(h, 2) * z[0] * distance
        assert (f_0, f_1) == (center + interaction, center - interaction)
        if not axial:
            assert f_0 == f_1  # The perpendicular line makes the cosh factor one.
        checked += 1
    print(f"{checked} exact balanced exponent factorizations")


def check_high_confidence_slopes():
    for size in range(4, 65):
        slopes = [F(8, max(a, size - a)) for a in range(1, size)]
        assert [a for a in range(1, size) if slopes[a - 1] == min(slopes)] == [1, size - 1]

    # A convergent rational series with a geometric tail bounds log(2).
    # log(2) = 2 sum_{k >= 0} (1/3)^(2k+1)/(2k+1).
    terms = 8
    partial = 2 * sum(F(1, (2*k+1) * 3**(2*k+1)) for k in range(terms))
    tail = F(2, (2*terms+1) * 3**(2*terms+1)) / (1 - F(1, 9))
    lower, upper = F(16, 3) + F(8, 3)*partial, F(16, 3) + F(8, 3)*(partial + tail)
    # Unequal 1--3 intercept at d=1 is 16/3 + (8/3) log(2).
    assert F("7.181725") < lower < upper < F("7.181726")
    print("61 exact slope comparisons and a rational bracket on the unequal intercept")


if __name__ == "__main__":
    check_likelihood_identity()
    check_expectation_certificate()
    check_balanced_geometry()
    check_high_confidence_slopes()
