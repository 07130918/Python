import logging
import multiprocessing
import time

logging.basicConfig(level=logging.DEBUG, format='%(processName)s: %(message)s')


def f(conn):
    # send()した時点でrecv()が受け取る
    conn.send(['test', 'sss'])
    time.sleep(2)
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=f, args=(parent_conn, ))
    p.start()
    print(p)
    logging.debug(child_conn.recv())
