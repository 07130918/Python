def something():
    print('Hi')
    return 'jump'


def what_is_this(color):
    print(color)
    if color == 'red':
        return 'tomato'
    else:
        return "I don't know"


result = something()
print(result)
what_is_this('red')
print(what_is_this('red'))
print(what_is_this('green'))
