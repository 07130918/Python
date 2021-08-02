def g_hello():
    while True:
        r = yield 'hello'
        yield r


g = g_hello()
print(next(g))
print(g.send('nick'))
print(next(g))
print(g.send('kota'))
