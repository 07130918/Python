int_list = [1, 10, 50, 100, 67]
print(int_list[::2])
print(int_list[::-1])

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 最後に追加
n.append(100)
print(n)

# 第1引数のインデックス番号に第2引数を追加
n.insert(1, 500)
print(n)

n.pop()
print(n)

n.pop(0)
print(n)

del n[1]
print(n)

# 引数に一致した最初のモノを削除
n.remove(7)
print(n)

x = [2, 2, 2, 2]
n.extend(x)
print(n)
