# 引数の順番に注意
def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)
    for key, val in kwargs.items():
        print(key, ':', val)


dic = {
    'entree': 'beef',
    'drink': 'soda',
    'dessert': 'ice'
}

tpl = ('juice', 'lemon')

menu('banana', 'apple', 'orange', entree='beef', drink='beer')
print('----------------------')
menu('chicken', *tpl, **dic)
