days = ['Mon', 'Tue', 'Wed']
drinks = ['coffee', 'milk', 'water']

dic = {}
for day, drink in zip(days, drinks):
    dic[day] = drink
print(dic)

dic = {key: value for key, value in zip(days, drinks)}
print(dic)
