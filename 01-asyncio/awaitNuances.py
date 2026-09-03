import asyncio
import time

async def fetch_data(x):
    print(f"Doing something with {x}")
    await asyncio.sleep(x)
    print(f"Done with {x}")
    return f"Result of {x}"

#When you await a task, it doesn't mean that it will start being executed first. But it guarantees that it's result will be returned first
async def main():
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    result2 = await task2
    print("Task 2 fully completed")
    result1 = await task1
    print("Task 1 fully completed")
    return [result1, result2]

t3 = time.perf_counter()
concurrent_results = asyncio.run(main())
print(concurrent_results)
t4 = time.perf_counter()
print(f"{t4-t3:.2f} s")