import re
"""
match()    文字列の先頭で正規表現にマッチするか判定
search()   文字列を操作して正規表現がどこにマッチするか調べる
findall()  正規表現にマッチする部分文字列を全て探し出しリストとして返す
finditer() 重複しないマッチオブジェクトのイテレータを返す
"""
m = re.match('a.c', 'abc')
print(m)
print(m.span())
print(m.group())

print('-' * 60)
m = re.search('a.c', 'test abc 080-7777-7777 abc')
print(m)
print(m.span())
print(m.group())

print('-' * 60)
m = re.findall('a.c', 'test abc 080-7777-7777 abc')
print(m)

print('-' * 60)
m = re.finditer('a.c', 'test abc 080-7777-7777 abc')
print(m)
print([w.group() for w in m])
