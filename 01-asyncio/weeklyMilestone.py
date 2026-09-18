import asyncio
import time
import httpx

URLS = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
]

def fetch(client, url):
    response = client.get(url)
    return response.status_code

def run_sequential():
    print("Running sequential requests")
    start = time.perf_counter()
    with httpx.Client(timeout=10.0) as client:
        for url in URLS:
            fetch(client, url)
    end = time.perf_counter()
    return f"Time it took for sequential = {(end-start):.2f}"


async def async_fetch(client, url):
    response = await client.get(url)
    return response.status_code

async def run_async(client):
    print("Running asynchronous requests")
    start = time.perf_counter()
    async with asyncio.TaskGroup() as tg:
        for url in URLS:
            tg.create_task(async_fetch(client, url))
    end = time.perf_counter()
    return f"Time it took for concurrent = {(end-start):.2f}"

async def main():
    seq_time = run_sequential()
    async with httpx.AsyncClient(timeout=10.0) as client:
        con_time = await run_async(client)
    print(seq_time)
    print(con_time)
if __name__ == "__main__":
    asyncio.run(main())
