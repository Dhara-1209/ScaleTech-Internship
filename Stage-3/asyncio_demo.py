import asyncio

async def task(name, seconds):

    print(name, "started")

    await asyncio.sleep(seconds)

    print(name, "finished")


async def main():

    await asyncio.gather(
        task("Task 1", 3),
        task("Task 2", 2),
        task("Task 3", 1)
    )


asyncio.run(main())