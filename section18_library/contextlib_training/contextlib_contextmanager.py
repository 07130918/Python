import contextlib

# def tag(name):
#     def _tag(f):
#         def _wrapper(content):
#             print(f'<{name}>')
#             f(content)
#             print(f'</{name}>')
#         return _wrapper
#     return _tag


# @tag('h2')
# def f(content):
#     print(content)


# f = tag('h2')(f)
# f('called')

@contextlib.contextmanager
def tag(name):
    print(f'<{name}>')
    yield
    print(f'</{name}>')


# @tag('h2')
# def f(content):
#     print(content)


# f('test')

with tag('h2'):
    print('test')
    with tag('span'):
        print('get caught in')
