import asyncio

loop = asyncio.get_event_loop()


class AwaitableClass(object):
    def __init__(self, name, loop):
        self.name = name
        self.loop = loop

    def __await__(self):
        """ Classがawaitで呼ばれた時に実行
        """
        @asyncio.coroutine
        def wrapper():
            reader, writer = yield from asyncio.open_connection(
                '127.0.0.1', 8888, loop=self.loop
            )
            writer.write(self.name.encode())
            writer.write_eof()
            data = yield from reader.read()
            data = int(data.decode())
            return data
        return (yield from wrapper())


class AsyncIterater(object):
    def __init__(self, name, loop):
        self.name = name
        self.loop = loop

    def __aiter__(self):
        """ Classがイテレータとして呼ばれた際に実行
        """
        return self

    async def __anext__(self):
        """ __aiter__のあとに非同期実行
        """
        data = await AwaitableClass(self.name, self.loop)
        if data < 0:
            raise StopAsyncIteration
        return data


class AsyncContextManager(object):
    def __init__(self, name, loop):
        self.enter = 'Enter'
        self.ac = AsyncIterater(name, loop)
        self.exit = 'Exit'

    async def __aenter__(self):
        print(self.enter)
        await asyncio.sleep(3)
        return self.ac

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(self.exit)
        await asyncio.sleep(3)


async def main(name, loop):
    print('chunk reader')
    # result = await AwaitableClass(name, loop)
    # async for i in AsyncIterater(name, loop):
    #     """ __anext__を繰り返し呼ぶ
    #     """
    #     print(i)
    async with AsyncContextManager(name, loop) as ac:
        # async with に入ると__aenter__を呼ぶ
        async for i in ac:
            print(i)


loop.run_until_complete(asyncio.wait([
    main('task 1', loop), main('task 2', loop)
]))
loop.close()
