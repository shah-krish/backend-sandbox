import asyncio
import time

def fetch_data(x):
    print(f"Input value is {x}")
    time.sleep(x)
    print(f"Finished with {x}")

def main():
    time1 = time.perf_counter()
    fetch_data(1)
    print(f"{1} completed")
    fetch_data(2)
    print(f"{2} completed")
    time2 = time.perf_counter()
    print(f"Completed in {time2-time1:.2f} s")

async def threadsMain():
    t1 = time.perf_counter()
    thread1 = asyncio.create_task(asyncio.to_thread(fetch_data,1))
    thread2 = asyncio.create_task(asyncio.to_thread(fetch_data,2))
    await thread1
    print(f"{1} completed")
    await thread2
    print(f"{2} completed")
    t2 = time.perf_counter()
    print(f"Completed in {t2 - t1:.2f} s")
main()
print(f"\n")
asyncio.run(threadsMain())