#!/usr/bin/env python3
""" 0x00-python_variable_annotations"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' return a function'''
    def mutiply(x: float) -> float:
        ''' mutiply by the multiplier'''
        return x * multiplier
    return mutiply
