#!/usr/bin/env python3
"""Async comprehension"""

import random
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    ''' using async for'''
    async def measure_runtime() -> float:
    """
    Async function that measures total run time
    and return it
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return end - start
