import functools


@functools.lru_cache(maxsize=5)
def long_func(n):
    r = 0
    for i in range(10000000):
        r += n * i
    return r


for i in range(10):
    print(long_func(i))
print(long_func.cache_info())
# long_func.cache_clear()

print('next run')

for i in reversed(range(10)):
    print(long_func(i))
print(long_func.cache_info())
