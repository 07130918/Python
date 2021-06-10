def outer(a, b):
    """
        return: inner関数(実行はしていない)を返す
    """
    def inner():
        return a + b

    return inner


func = outer(4, 13)
print(func)

# inner関数はここで実行される(func())
result = func()
print(result)


def circle_area_func(pi):

    def circle_area(radius):
        return pi * radius ** 2

    return circle_area


ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.1415926539)

print(ca1(10))
print(ca2(10))
