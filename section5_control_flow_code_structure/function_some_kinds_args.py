def menu(entree='chicken', drink='wine', dessert='pudding'):
    print(entree)
    print(drink)
    print(dessert)


menu('beef', dessert='ice', drink='beer')
print('-------------------')
menu()

# Pythonでは空リストをデフォルト引数にすべきではない


def lst_append(x, lst=[]):
    lst.append(x)
    return lst


def lst_none_append(x, lst=None):
    if lst is None:
        lst = []
    lst.append(x)
    return lst


print(lst_append(100, [1, 2, 3]))

print(lst_append(100, [1, 2, 3]))

print('-------------------')

print(lst_append(500))

print(lst_append(100))

print('-------------------')

print(lst_none_append(500))

print(lst_none_append(100))
