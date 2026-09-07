import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

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

async def processesMain():
    t1 = time.perf_counter()
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as executor:
        process1 = loop.run_in_executor(executor,fetch_data,1)
        process2 = loop.run_in_executor(executor,fetch_data,2)
        await process1
        print(f"{1} completed")
        await process2
        print(f"{2} completed")
        t2 = time.perf_counter()
        print(f"Completed in {t2 - t1:.2f} s")

if __name__ == "__main__":
    main()
    print(f"\n")
    asyncio.run(threadsMain())
    print(f"\n")
    asyncio.run(processesMain())