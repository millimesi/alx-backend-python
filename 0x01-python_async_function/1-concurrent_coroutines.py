#!/usr/bin/env python3
'''0x01-python_async_function'''

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    ''' Wait multiple time'''
    waits = []
    for _ in range(n):
        waits.append(wait_random(max_delay))
    delays = await asyncio.gather(*waits)
    return sorted(delays)
