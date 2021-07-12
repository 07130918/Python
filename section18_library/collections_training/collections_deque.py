import collections
import queue

q = queue.Queue()
lq = queue.LifoQueue()
l = []
d = collections.deque()

for i in range(3):
    q.put(i)
    lq.put(i)
    l.append(i)
    d.append(i)

for _ in range(3):
    print(f'FIFO queue = {q.get()}')
    print(f'LIFO queue = {lq.get()}')
    print(f'list       = {l.pop(0)}')
    print(f'deque      = {d.popleft()}')
    print()


d = collections.deque()
for i in range(3):
    d.append(i)

print(d)
d.rotate()
print(d)
d.rotate()
print(d)
d.rotate()
d.extendleft('X')
d.extend('Y')
print(d)
