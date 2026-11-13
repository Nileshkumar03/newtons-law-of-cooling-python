
import numpy as np

def cooling_model(t, T0, Ts, k):
    """
    Newton's Law of Cooling.

    t  : Time
    T0 : Initial temperature
    Ts : Surrounding temperature
    k  : Cooling constant
    """

    return Ts + (T0 - Ts) * np.exp(-k * t)
