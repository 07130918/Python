import tarfile

# tarの作成
with tarfile.open('material/test.tar.gz', 'w:gz') as tr:
    tr.add('material/test_dir')

# tarの展開
with tarfile.open('material/test.tar.gz', 'r:gz') as tr:
    # tr.extractall(path='test_tar')
    with tr.extractfile('material/test_dir/sub_dir/sub_test.txt') as f:
        print(f.read())
