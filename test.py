import time
import asyncio

def job(t):
    print('Start job ', t)
    time.sleep(t)               # wait for "t" seconds
    print('Job ', t, ' takes ', t, ' s')


def main():
    [job(t) for t in range(1, 3)]


t1 = time.time()
main()
print("NO async total time : ", time.time() - t1)

async def job(t):                   # async 形式的功能
    print('Start job ', t)
    await asyncio.sleep(t)          # 等待 "t" 秒, 期间切换其他任务
    print('Job ', t, ' takes ', t, ' s')


async def main(loop):                       # async 形式的功能
    tasks = [
    loop.create_task(job(t)) for t in range(1, 3)
    ]                                       # 创建任务, 但是不执行
    await asyncio.wait(tasks)               # 执行并等待所有任务完成

t1 = time.time()
loop = asyncio.get_event_loop()             # 建立 loop
loop.run_until_complete(main(loop))         # 执行 loop
loop.close()                                # 关闭 loop
print("Async total time : ", time.time() - t1)