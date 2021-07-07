import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1():
    logging.debug('worker1 start')
    # print(threading.current_thread().getName(), 'start')
    time.sleep(2)
    logging.debug('worker1 end')
    # print(threading.current_thread().getName(), 'end')


def worker2(x, y=1):
    print(threading.current_thread().getName(), ':worker2: start')
    logging.debug(x)
    logging.debug(y)
    time.sleep(2)
    print(threading.current_thread().getName(), ':worker2: end')


if __name__ == '__main__':
    t1 = threading.Thread(name='rename worker1', target=worker1)
    t2 = threading.Thread(target=worker2, args=(100, ), kwargs={'y': 200})
    t1.start()
    t2.start()
    print('started')
