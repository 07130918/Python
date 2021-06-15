with open('test.txt', 'r') as f:
    # seekで読み込み開始位置を操る
    print(f.tell())
    print(f.read(1))
    f.seek(5)
    print(f.read(3))
    f.seek(0)
    print(f.read(4))
