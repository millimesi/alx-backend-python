#!/usr/bin/env python3
""" 0x00-python_variable_annotations"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' Sum up mixed list of float and intege'''
    return sum(mxd_lst)
