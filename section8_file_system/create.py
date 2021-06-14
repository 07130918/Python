f = open('test.txt', 'w')
f.write('test\n')
print("Hello text file", file=f)
print('My', 'name', 'is', 'kota', sep='#', end='!', file=f)
f.close()

# ブロックでファイル作業は行う
with open('test.txt', 'w') as f:
    print("------------", file=f)
    f.write('test\n')
    print("Hello text file", file=f)
    print('My', 'name', 'is', 'kota', sep='#', end='!', file=f)
