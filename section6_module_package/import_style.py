# 1.標準ライブラリ
import collections
import os
import sys

# 2. 3rd partyライブラリ
import termcolor

# 3.チームが開発したもの
import l_package

# 4.自分が開発したもの
import config

print(collections.__file__)
print(os.getcwd())
print(sys.path)
print('---------------')
print(termcolor.__file__)
print(l_package)
print(config.__file__)
