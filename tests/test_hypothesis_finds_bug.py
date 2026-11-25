"""A bug that hypothesis finds and a hand-written test does not.

Boltzmann populations of a set of conformers, p_i = exp(-E_i/kT) / sum_j
exp(-E_j/kT), computed naively. The hand-written test below uses small relative
energies and passes. Hypothesis also tries energies like those a DFT code
prints (total energies of hundreds or thousands of eV), where exp() overflows
or underflows and the populations come out as NaN.

The hypothesis test of the naive version is marked xfail so the suite stays
clean. Delete the @pytest.mark.xfail line and run `pixi run test` to see the
input hypothesis found.
"""

import numpy as np
import pytest
from hypothesis import given
from hypothesis import strategies as st
from numpy.typing import ArrayLike, NDArray

KT_ROOM_TEMPERATURE_EV = 0.025852  # k_B * 300 K in eV


def naive_populations(energies: ArrayLike, kt: float) -> NDArray[np.float64]:
    """Boltzmann populations, straight from the textbook formula."""
    weights = np.exp(-np.asarray(energies, dtype=np.float64) / kt)
    return weights / float(weights.sum())


def stable_populations(energies: ArrayLike, kt: float) -> NDArray[np.float64]:
    """Boltzmann populations, measuring energies from the lowest one.

    Shifting all energies by a constant does not change the populations, and
    after the shift the largest weight is exp(0) = 1, so nothing overflows and
    the sum is at least 1.
    """
    e = np.asarray(energies, dtype=np.float64)
    weights = np.exp(-(e - e.min()) / kt)
    return weights / float(weights.sum())


# Tells hypothesis to make a list of energies between -1e4 and 1e4 eV, with 1 to
# 10 elements.
dft_energies = st.lists(
    st.floats(min_value=-1e4, max_value=1e4), min_size=1, max_size=10
)


def assert_valid_populations(p: NDArray[np.float64]) -> None:
    assert np.all(np.isfinite(p)), f"populations are not finite: {p}"
    assert np.all(p >= 0), f"negative populations: {p}"
    assert p.sum() == pytest.approx(1.0)


# The test one would write by hand: relative energies of a few conformers.
# It passes, and the naive formula looks fine.
def test_naive_populations_by_hand() -> None:
    p = naive_populations([0.0, 0.05, 0.1], KT_ROOM_TEMPERATURE_EV)
    assert_valid_populations(p)
    assert p[0] > p[1] > p[2]


# The same property checked on many inputs. Hypothesis finds energies where the
# naive formula returns NaN, and shrinks them to a minimal example.
@pytest.mark.xfail(reason="exp() overflows or underflows for large energies")
# numpy warns about the 0/0 that produces the NaN; hide it while the test is xfail.
@pytest.mark.filterwarnings("ignore::RuntimeWarning")
@given(dft_energies)
def test_naive_populations(energies: list[float]) -> None:
    assert_valid_populations(naive_populations(energies, KT_ROOM_TEMPERATURE_EV))


@given(dft_energies)
def test_stable_populations(energies: list[float]) -> None:
    assert_valid_populations(stable_populations(energies, KT_ROOM_TEMPERATURE_EV))
