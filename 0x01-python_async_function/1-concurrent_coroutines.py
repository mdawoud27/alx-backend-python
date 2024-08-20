#!/usr/bin/env python3
"""1. Let's execute multiple coroutines at the same time with async"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """function that return the list of all the delays (float values)."""
    delay_list: list[float] = []
    for _ in range(n):
        delay_list.append(await wait_random(max_delay))
    return sorted(delay_list)
