#!/usr/bin/env python3
'''0x01-python_async_function'''

import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n, max_delay):
    ''' Wait multiple time'''
    waits = []
    for _ in range(n):
        waits.append(task_wait_random(max_delay))
    delays = await asyncio.gather(*waits)
    return sorted(delays)
