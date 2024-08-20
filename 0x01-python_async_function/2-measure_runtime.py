#!/usr/bin/env python3
"""2. Measure the runtime"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Function measures the total execution time for wait_n"""
    begin: float = time.perf_counter()
    await wait_n(n, max_delay)
    total_time: float = time.perf_counter() - begin

    return total_time / n
