string = 'Hi. This is Kota'

is_start = string.startswith('Hello')

print(is_start)
print(string.find('Kota'))
# 引数が最後に出てきたインデックス番号を返す
print(string.rfind('i'))
print(string.count('i'))
# 始まり以外を小文字に
print(string.capitalize())
# 単語の始まりを大文字に
print(string.title())
print(string.lower())
print(string.replace('Kota', 'Kim'))
