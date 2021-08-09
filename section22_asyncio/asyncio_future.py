import asyncio

loop = asyncio.get_event_loop()


async def f(future):
    await asyncio.sleep(1)
    future.set_result('Future is done!!!')


def got_result(future):
    print(future.result())
    loop.stop()


future = asyncio.Future()
asyncio.ensure_future(f(future))

# loop.run_until_complete(future)
# print(future.result())

future.add_done_callback(got_result)

loop.run_forever()
loop.close()
