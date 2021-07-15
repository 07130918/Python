import collections

a = {'a': 'a', 'c': 'c', 'num': 0}
b = {'b': 'b', 'c': 'cc'}
c = {'b': 'bbb', 'c': 'ccc'}

# print(a)
# a.update(b)
# print(a)
# a.update(c)
# print(a)

m = collections.ChainMap(a, b, c)
print(m)
print(m.maps)
print(m['c'])

print('-' * 60)
m.maps.reverse()
print(m.maps)
print(m['c'])

print('-' * 60)
m.maps.insert(0, {'c': 'CCCC'})
print(m.maps)
print(m['c'])


class DeepChainMap(collections.ChainMap):

    def __setitem__(self, key, value):
        for mapping in self.maps:
            if key in mapping:
                if type(mapping[key]) is int and mapping[key] < value:
                    mapping[key] = value
                return
        self.maps[0][key] = value


m = DeepChainMap(a, b, c)
m['num'] = 99
print(m['num'])
m['num'] = 55
print(m['num'])
m['print'] = 1000
print(m)
print(m['print'])
