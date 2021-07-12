import contextlib
import os

try:
    os.remove('somefile.py')
except FileNotFoundError:
    print('into except')


with contextlib.suppress(FileNotFoundError):
    os.remove('somefile.py')
    print('suppress')
