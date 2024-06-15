#!/usr/bin/env python3
""" 0x00-python_variable_annotations"""

from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' Duck type annotation in seqquence and Iterable'''
    return [(i, len(i)) for i in lst]
