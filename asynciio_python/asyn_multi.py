import  asyncio
import timeit

async def crwal_page(url):
    print('crwaling {}'.format(url))
    sleep_time = int (url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('Ok {}'.format(url))

async  def main(urls):
    for url in urls:
        await  crwal_page(url)



timeit asyncio.run(main(['url_1','url_2','url_3','url_4']))


async  def  worker_1():
    await asyncio.sleep(1)
    return 1

async  def  worker_2():
    await asyncio.sleep(2)
    return 2/0
async def worker_3() :
    await  asyncio.sleep(3)
    return 3


async def main ():
    task_1 = asyncio.create_task(worker_1())
    task_2 = asyncio.create_task(worker_2())
    task_3 = asyncio.create_task(worker_3())

    await  asyncio.sleep(2)
    task_3.cancel()

    res  = await asyncio.gather(task_1,task_2,task_3,return_exceptions=True)

    print(res)

%time asyncio.run(main())

##输出
# [1,ZeroDivisionError('division by zero') , CancelledError()]



