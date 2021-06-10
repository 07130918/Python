def gene():
    for i in range(10):
        yield i


g = gene()
print(next(g))
print(next(g))
print(next(g))

g = (i for i in range(10) if i % 2 == 0)
print(type(g))
print(g)
print(next(g))
print(next(g))
print(next(g))

# tupleはgeneratorと似ているため注意
t = tuple(i for i in range(10) if i % 2 == 0)
print(type(t))
print(t)
