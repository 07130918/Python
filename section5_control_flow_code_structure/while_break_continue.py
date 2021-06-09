count = 0
while count < 5:
    print(count)
    count += 1

print('-------------------')

count = 0
while True:
    if count >= 5:
        break
    if count == 2:
        count += 1
        # 下の処理に行かず次のループへ
        continue
    print(count)
    count += 1
