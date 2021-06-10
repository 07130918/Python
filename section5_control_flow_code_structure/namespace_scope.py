animal = 'cat'


def f():
    # Pythonは関数内から外の変数にアクセス可能
    print('animal:', animal)


def fun():
    global animal
    animal = 'dog'
    drink = 'coffee'
    print('animal:', animal)
    print('locals:', locals())


f()
fun()
f()
print('globals:', animal)
print(globals())
