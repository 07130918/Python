import asyncio

loop = asyncio.get_event_loop()

def hello(name, loop):
    print(f'Hello {name}')
    loop.stop()

loop.call_later(2, hello, 'Mike', loop)
loop.call_soon(hello, 'Kota', loop)

loop.run_forever()
loop.close()
