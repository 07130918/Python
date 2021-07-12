import collections

d = {}
l = ['a', 'a', 'a', 'b', 'b', 'c']
for word in l:
    if word not in d:
        d[word] = 0
    d[word] += 1
print(d)

d = {}
l = ['a', 'a', 'a', 'b', 'b', 'c']
for word in l:
    d.setdefault(word, 0)
    d[word] += 1
print(d)

print('-' * 60)
d = collections.defaultdict(int)
print(d)
l = ['a', 'a', 'a', 'b', 'b', 'c']
for word in l:
    d[word] += 1
print(d)

print('-' * 60)
d = collections.defaultdict(set)
print(d)
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4),
     ('red', 1), ('blue', 4), ]
for color, val in s:
    d[color].add(val)
print(d)
