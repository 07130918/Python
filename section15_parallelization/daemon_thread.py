import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1():
    logging.debug('worker1 start')
    time.sleep(5)
    logging.debug('worker1 end')


def worker2():
    logging.debug('worker2 start')
    time.sleep(2)
    logging.debug('worker2 end')


if __name__ == '__main__':
    t1 = threading.Thread(target=worker1)
    t1.setDaemon(True)
    t2 = threading.Thread(target=worker2)
    t1.start()
    t2.start()
    print('started')
    # ↓wait for t1 thread end
    t1.join()
