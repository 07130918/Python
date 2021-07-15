import functools


def f(x, y):
    return x + y


def task(func):
    print('start')
    print(func())


# def outer(x, y):
#     def inner():
#         return x + y
#     return inner


# func_ob = outer(10, 20)
# task(func_ob)

p = functools.partial(f, 10, 20)
task(p)
