import asyncio
import random
import time


async def consumer(quene, id):
    while True:
        val = await  quene.get()
        print('{} get a val: {}'.format(id, val))
        await  asyncio.sleep(1)


async def producer(quene, id):
    for i in range(5):
        val = random.randint(1, 10)
        await quene.put(val)
        print('{} put a val : {}'.format(id, val))
        await asyncio.sleep(1)


async def main():
    quene = asyncio.Queue()
    consumer_1 = asyncio.create_task(consumer(quene, 'consumer_1'))
    consumer_2 = asyncio.create_task(consumer(quene, 'consumer_2'))

    producer_1 = asyncio.create_task(producer(quene, 'producer_1'))
    producer_2 = asyncio.create_task(producer(quene, 'producer_2'))

    await asyncio.sleep(10)
    consumer_1.cancel()
    consumer_2.cancel()

    await  asyncio.gather(consumer_1, consumer_2, producer_1, producer_2, return_exceptions=True)

asyncio.run(main())
