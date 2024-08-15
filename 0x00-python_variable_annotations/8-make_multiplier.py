#!/usr/bin/env python3
"""
8. Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes a float multiplier as argument and returns a function
    that multiplies a float by multiplier.
    Args:
        multiplier (float): a float number
    Return:
        a function that multiplies a float by multiplier.
    """
    def multiply(value: float) -> float:
        return value * multiplier

    return multiply
