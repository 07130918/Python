import glob
import zipfile

# zipの作成
with zipfile.ZipFile('test.zip', 'w') as z:
    # z.write('test_dir')
    # z.write('test_dir/text.txt')
    for f in glob.glob('test_dir/**', recursive=True):
        print(f)
        z.write(f)

# zipの展開
with zipfile.ZipFile('test.zip', 'r') as z:
    # z.extractall('zip_dep')
    with z.open('test_dir/sub_dir/sub_test.txt') as f:
        print('--------------')
        print(f.read())
