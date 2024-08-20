#!/usr/bin/env python3
"""2. Run time for four parallel comprehensions"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime should measure the total runtime and return it."""
    begin = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - begin
