"""Example tests: one known value, and one property checked on many inputs."""

import numpy as np
import pytest
from hypothesis import given
from hypothesis import strategies as st

from mypackage.units import HARTREE_IN_EV, ev_to_hartree, hartree_to_ev


# Test that one hartree is correctly converted to eV
def test_one_hartree() -> None:
    assert hartree_to_ev(1.0) == pytest.approx(HARTREE_IN_EV)


# Pytest test that checks tha tthe conversion functions work on arrays. 
def test_works_on_arrays() -> None:
    energies = np.array([0.0, 1.0, 2.0])
    np.testing.assert_allclose(ev_to_hartree(hartree_to_ev(energies)), energies)


# Test that converting from hartree to eV and back is approximately the identity function
# Hypothesis will generate a wide range of float values to test the roundtrip conversion
@given(st.floats(min_value=-1e6, max_value=1e6))
def test_roundtrip(energy: float) -> None:
    assert hartree_to_ev(ev_to_hartree(energy)) == pytest.approx(energy)
