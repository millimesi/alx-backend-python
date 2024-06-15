#!/usr/bin/env python3
'''0x01-python_async_function'''

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    ''' Wait multiple time'''
    waits = []
    for _ in range(n):
        waits.append(wait_random(max_delay))
    delays = await asyncio.gather(*waits)
    return sorted(delays)
