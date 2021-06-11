dic = {'abc': 100, 200: 'old'}
print(dic[200])

print(dic.values())

dic = {}
dic["このように"] = "値をset"
print(dic)
# dic.clear()

c = {'abc': 'yyy', 'color': 'red'}

# オーバーライド
dic.update(c)
print(dic)

# keyの判定
print('abc' in dic)
