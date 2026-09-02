import asyncio
import time

async def fetch_data(x):
    print(f"Doing something with {x}")
    await asyncio.sleep(x)
    print(f"Done with {x}")
    return f"Result of {x}"

#coroutine function but using coroutine (not really concurrent) instead of tasks
async def main():
    task1 = fetch_data(1)
    task2 = fetch_data(2)
    result1 = await task1
    print("Task 1 fully completed")
    result2 = await task2
    print("Task 2 fully completed")
    return [result1, result2]

#coroutine function utilizing tasks which can be scheduled concurrently on the event loop
async def main2():
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    result1 = await task1
    print("Task 1 fully completed")
    result2 = await task2
    print("Task 2 fully completed")
    return [result1, result2]

t1 = time.perf_counter()
results = asyncio.run(main())
print(results)
t2 = time.perf_counter()
print(f"{t2-t1:.2f} s")

t3 = time.perf_counter()
concurrent_results = asyncio.run(main2())
print(results)
t4 = time.perf_counter()
print(f"{t4-t3:.2f} s")


