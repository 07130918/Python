import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1(d, lock):
    logging.debug('worker1 start')
    with lock:
        d['x'] += 1
        time.sleep(2)
        logging.debug(d)
        with lock:
            d['x'] += 1
            time.sleep(1)
            logging.debug(d)
    logging.debug('worker1 end')


def worker2(d, lock):
    logging.debug('worker2 start')
    lock.acquire()
    d['x'] += 1
    logging.debug(d)
    lock.release()
    logging.debug('worker2 end')


if __name__ == '__main__':
    d = {'x': 0}
    lock = threading.RLock()
    t1 = threading.Thread(target=worker1, args=(d, lock))
    t2 = threading.Thread(target=worker2, args=(d, lock))
    t1.start()
    t2.start()
    print('started')
