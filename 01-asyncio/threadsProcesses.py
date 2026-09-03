import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

#Synchronous function
def fetch_data(param):
    print(f"Do something with {param}...", flush=True)
    time.sleep(param)
    print(f"Done with {param}", flush=True)
    return f"Result of {param}"

async def main():
    task1 = asyncio.create_task(asyncio.to_thread(fetch_data, 1))
    task2 = asyncio.create_task(asyncio.to_thread(fetch_data,2))
    result1 = await task1
    print("Thread one completed")
    result2 = await task2
    print("Thread two completed")

    #We need to manually attach processes to loop so we fetch it
    loop = asyncio.get_running_loop()

    with ProcessPoolExecutor() as executor:
        #Since new process doesn't have any shared memory, we have to provide it
        task1 = loop.run_in_executor(executor, fetch_data,1)
        task2 = loop.run_in_executor(executor, fetch_data, 2)

        result1 = await task1
        print("Process one completed")
        result2 = await task2
        print("Process two completed")

    return [result1, result2]

#We need this to block infinite loop when using processes
if __name__ == "__main__":
    t1 = time.perf_counter()

    results = asyncio.run(main())
    print(results)

    t2 = time.perf_counter()
    print(f"Finished in {t2 - t1:.2f} seconds")