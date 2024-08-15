#!/usr/bin/env python3
"""
10. Duck typing - first element of a sequence
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely returns the first element of a sequence or None if
    the sequence is empty.
    Args:
        lst (Sequence[Any]): A sequence (list, tuple, etc.) of
        elements of any type.
    Returns:
        Union[Any, None]: The first element of the sequence if
        it is not empty, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
