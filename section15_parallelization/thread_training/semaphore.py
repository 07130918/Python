import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1(semaphore):
    with semaphore:
        logging.debug('worker1 start')
        time.sleep(3)
        logging.debug('worker1 end')


def worker2(semaphore):
    with semaphore:
        logging.debug('worker2 start')
        time.sleep(3)
        logging.debug('worker2 end')


def worker3(semaphore):
    with semaphore:
        logging.debug('worker3 start')
        time.sleep(3)
        logging.debug('worker3 end')


if __name__ == '__main__':
    # threadの定員を決められる
    semaphore = threading.Semaphore(2)
    t1 = threading.Thread(target=worker1, args=(semaphore, ))
    t2 = threading.Thread(target=worker2, args=(semaphore, ))
    t3 = threading.Thread(target=worker3, args=(semaphore, ))
    t1.start()
    t2.start()
    t3.start()
    print('started')
