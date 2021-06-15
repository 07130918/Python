chunk = 7

with open('test.txt', 'r') as f:
    # print(f.read())
    while True:
        line = f.read(chunk)
        print(line)
        if not line:
            break
