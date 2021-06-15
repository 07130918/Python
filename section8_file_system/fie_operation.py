import os
import pathlib
import glob
import shutil

print(os.path.exists('test.txt'))
print(os.path.isfile('test.txt'))
print(os.path.isdir('dir'))
# os.symlink('test.txt', 'symlink.txt')

os.mkdir('test_dir')
os.rmdir('test_dir')

pathlib.Path('empty.txt').touch()
os.remove('empty.txt')

print(os.listdir('__pycache__'))
shutil.copy('__pycache__/csv.cpython-38.pyc', '__pycache__/index.pyc')
print(glob.glob('__pycache__/*'))
# shutil.rmtree('__pycache__')
