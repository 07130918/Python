greeting_list = ['Good morning', 'Good afternoon', 'Good night']

for i in greeting_list:
    print(i)

print('-----------')


def greeting():
    yield 'Good morning'
    print('Hello!!!')
    yield 'Good afternoon'
    yield 'Good night'


def counter(num=10):
    for _ in range(num):
        yield 'run'


for i in greeting():
    print(i)

print('-----------')

g = greeting()
c = counter()

print(next(g))
print(next(c))
print(next(c))
print('hi')
print(next(g))
print(next(c))
print(next(c))
print('hi')
print(next(g))
