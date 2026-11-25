"""Energy unit conversions: an example module, replace it with your own code."""

import numpy as np
from numpy.typing import ArrayLike, NDArray

HARTREE_IN_EV = 27.211386245988
"""CODATA 2018 value of one hartree in electronvolts."""


# Try removing "ArrayLike" and then run pixi r typecheck. 
def ev_to_hartree(energy: ArrayLike) -> NDArray[np.float64]:
    """Convert energies from electronvolts to hartree."""
    return np.asarray(energy, dtype=np.float64) / HARTREE_IN_EV


def hartree_to_ev(energy: ArrayLike) -> NDArray[np.float64]:
    """Convert energies from hartree to electronvolts."""
    return np.asarray(energy, dtype=np.float64) * HARTREE_IN_EV
