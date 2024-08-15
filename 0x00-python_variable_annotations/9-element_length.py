#!/usr/bin/env python3
"""
9. Let's duck type an iterable object
"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
       Takes a list of sequences and returns a list of tuples.
       Each tuple contains a sequence and its corresponding length.

       Args:
           lst (Iterable[Sequence]): An iterable of sequences.

       Returns:
           List[Tuple[Sequence, int]]: A list of tuples where each tuple
           contains a sequence and its length.
   """
    return [(i, len(i)) for i in lst]
