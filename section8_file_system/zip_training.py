import glob
import zipfile

# zipの作成
with zipfile.ZipFile('material/test.zip', 'w') as z:
    # z.write('material/test_dir')
    # z.write('material/test_dir/text.txt')
    for f in glob.glob('material/test_dir/**', recursive=True):
        print(f)
        z.write(f)

# zipの展開
with zipfile.ZipFile('material/test.zip', 'r') as z:
    # z.extractall('zip_dep')
    with z.open('material/test_dir/sub_dir/sub_test.txt') as f:
        print('--------------')
        print(f.read())
