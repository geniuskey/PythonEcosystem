import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    # 두 개의 코루틴을 동시에 실행합니다.
    await asyncio.gather(
        say_after(1, 'hello'),
        say_after(2, 'world')
    )

    print(f"finished at {time.strftime('%X')}")

# Python 3.7 이상에서는 asyncio.run()을 사용하여 main 코루틴을 실행할 수 있습니다.
asyncio.run(main())
