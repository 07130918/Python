dic = {'abc': 100, 200: 'old'}
print(dic[200])

print(dic.values())

c = {'abc': 'yyy', 'color': 'red'}

# オーバーライド
dic.update(c)
print(dic)

print('abc' in dic)
