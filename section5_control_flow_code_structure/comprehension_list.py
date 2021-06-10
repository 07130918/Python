t = (1, 2, 3, 4, 5, 6)
t2 = (7, 8, 9, 10, 11, 12)

r = []
for i in t:
    if i % 2 == 0:
        r.append(i)
print(r)

r = [i for i in t if i % 2 == 0]
print(r)

r = []
for i in t:
    for j in t2:
        r.append(i * j)

print(r)

# forループがネストする場合は基本的に使わない
r = [i * j for i in t for j in t2]

print(r)
