days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer', 'macha']

for day, fruit, drink in zip(days, fruits, drinks):
    print(f'{day}: {drink}を飲んで,{fruit}を食べた')
