def say_something(word, *args):
    print(word)
    print(args)
    for arg in args:
        print(arg)


say_something('Hi', 'Kota', 'Naruto', 'Ohtani')
print('---------------------')
tpl = ('Mike', 'Jon', 'Nancy')
say_something('Hi', *tpl)
