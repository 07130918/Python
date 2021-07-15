import collections
import re

d = collections.defaultdict(int)
print(d)
l = ['a', 'a', 'a', 'b', 'b', 'c']
for word in l:
    d[word] += 1
print(d)

print('-' * 60)
l = ['a', 'a', 'a', 'b', 'b', 'c']
c = collections.Counter()
print(c)
for word in l:
    c[word] += 1
print(c)
print(c.most_common(2))
print(sum(c.values()))


print('-' * 60)
with open('collections_counter.py', 'r') as f:
    words = re.findall(r'\w+', f.read().lower())
    print(collections.Counter(words).most_common(20))
