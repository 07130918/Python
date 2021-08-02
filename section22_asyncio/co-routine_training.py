def g_hello():
    while True:
        r = yield 'hello'
        yield r


def hello():
    yield 'hello 1'
    yield 'hello 2'
    yield 'hello 3'
    return 'done'


def g_hello_from():
    """ fromを使うことでジェネレーターからraiseが上がらないようにする
    """
    while True:
        r = yield from hello()
        yield r


g = g_hello()
print(next(g))
print(g.send('nick'))
print(next(g))
print(g.send('kota'))

print('-' * 60)

f = g_hello_from()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
