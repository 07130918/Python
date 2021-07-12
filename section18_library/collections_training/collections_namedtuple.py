import collections

Point = collections.namedtuple('Point', ['x', 'y'])

p = Point(10, 20)
print(p)
print(p.x)

print('-' * 60)
p1 = Point._make([100, 200])
print(p1)
print(p1._asdict())

print('-' * 60)
p1._replace(x=500)
print(p1)
p2 = p1._replace(x=500)
print(p2)


class SumPoint(collections.namedtuple('Point', ['x', 'y'])):
    @property
    def total(self):
        return self.x + self.y


p3 = SumPoint(2, 3)
print(p3.total)
