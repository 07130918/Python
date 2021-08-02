import concurrent.futures
import os
import time

"""
IO bound: syncよりもthreadもprocessも早く終わる
CPU bound: threadは不得意
"""

LEARGE_TEXT = 'some string' * 10000000


def io_bound(file_name):
    with open(file_name, 'w+') as f:
        f.write(LEARGE_TEXT)
        f.seek(0)
        f.read

    os.remove(file_name)
    return 'Future is done!'


def cpu_bound():
    i = 0
    while i < 10000000:
        i = i + 1 - 2 + 3 - 4 + 5
    return 'Future is done'


if __name__ == '__main__':
    # シンプルに呼び出す
    start = time.time()
    print(io_bound('1.txt'))
    print(io_bound('2.txt'))
    end = time.time()
    print(f'I/O bound: Sync {(end - start):.4f}')

    # thread使用
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        start = time.time()
        future1 = executor.submit(io_bound, '1.txt')
        future2 = executor.submit(io_bound, '2.txt')
        print(future1.result())
        print(future2.result())
        end = time.time()
        print(f'I/O bound: Thread {(end - start):.4f}')

    # process使用
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        start = time.time()
        future1 = executor.submit(io_bound, '1.txt')
        future2 = executor.submit(io_bound, '2.txt')
        print(future1.result())
        print(future2.result())
        end = time.time()
        print(f'The number of cpu: {os.cpu_count()}')
        print(f'I/O bound: Process {(end - start):.4f}')

    print('-' * 60)

    start = time.time()
    # シンプルに呼び出す
    print(cpu_bound())
    print(cpu_bound())
    end = time.time()
    print(f'CPU bound: Sync {(end - start):.4f}')

    # thread使用
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        start = time.time()
        future1 = executor.submit(cpu_bound)
        future2 = executor.submit(cpu_bound)
        print(future1.result())
        print(future2.result())
        end = time.time()
        print(f'CPU bound: Thread {(end - start):.4f}')

    # process使用
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        start = time.time()
        future1 = executor.submit(cpu_bound)
        future2 = executor.submit(cpu_bound)
        print(future1.result())
        print(future2.result())
        end = time.time()
        print(f'The number of cpu: {os.cpu_count()}')
        print(f'CPU bound: Process {(end - start):.4f}')
