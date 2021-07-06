import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1():
    logging.debug('start')
    # print(threading.current_thread().getName(), 'start')
    time.sleep(2)
    logging.debug('end')
    # print(threading.current_thread().getName(), 'end')


def worker2():
    print(threading.current_thread().getName(), 'start')
    time.sleep(3)
    print(threading.current_thread().getName(), 'end')


if __name__ == '__main__':
    t1 = threading.Thread(target=worker1)
    t2 = threading.Thread(target=worker2)
    t1.start()
    t2.start()
    print('started')
