lst = [1, 2, 3]
i = 5

try:
    print('try now')
    # del typo
    # lst[i]
    20 / 0
except IndexError as cause:
    print(f"Don't worry: {cause}")
except NameError as why:
    print(f"Failure because: {why}")
    # ExceptionはIndexErrorなどの親
except Exception as other:
    print(f'その他例外発生: {other}')
else:
    # try節が成功したらelseに来る
    print('well done')
finally:
    print('clean up')

print('end')
