string = 'a is {}'.format('test')
print(string)

string = 'a is {0} {2} {1}'.format('apple', 123, 'orange')
print(string)

string = '背番号{number}, {color}team'.format(color='blue', number=12)
print(string)

color = 'red'
number = 1
print(f'背番号{number}, {color}team')

# 型変換
s = str(1)
print(type(s))
