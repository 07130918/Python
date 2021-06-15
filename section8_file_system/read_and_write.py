s = """\
test
Hello text file
My#name#is#kota!
"""

with open('test.txt', 'w+') as f:
    f.write(s)
    f.seek(0)
    print(f.read())

print('-------------------')
# w+との違いはファイルがないと作るのではなくエラーになる
with open('test.txt', 'r+') as f:
    print(f.read())
    f.seek(0)
    f.write(s)
