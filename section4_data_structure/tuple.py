# tuple型は基本的に後から変更できない
t = (1, 2, 3, 4, 5)
print(t[-1])

# unpacking
num_tuple = (7, 9)
print(num_tuple)

x, y = num_tuple
print(x, y)

a = 100
b = 200
b, a = a, b
print(a, b)
