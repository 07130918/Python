class UppercaseError(Exception):
    pass


def check():
    words = ['APPLE', 'banana', 'orange']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)


try:
    check()
except UppercaseError as exc:
    print(f'This is my fault: UppercaseError -> {exc}')
finally:
    print('Go next!')
