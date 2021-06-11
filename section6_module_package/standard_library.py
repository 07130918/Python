from collections import defaultdict

s = "fvbnfgbjngbfgsjpnbf"

dic = {}
for c in s:
    if c not in dic:
        dic[c] = 0
    dic[c] += 1
print(dic)

dic = {}
for c in s:
    if c not in dic:
        dic.setdefault(c, 0)
    dic[c] += 1
print(dic)

dic = defaultdict(int)

for c in s:
    dic[c] += 1
print(dic)
