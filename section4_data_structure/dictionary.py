dic = {'abc': 100, 200: 'old'}
print(dic[200])

print(dic.values())

c = {'abc': 'yyy', 'color': 'red'}

dic = {}
dic["このように"] = "値をset"
print(dic)
dic.clear()

# オーバーライド
dic.update(c)
print(dic)

print('abc' in dic)
