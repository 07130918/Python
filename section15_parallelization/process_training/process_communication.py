import logging
import multiprocessing
import time

logging.basicConfig(level=logging.DEBUG, format='%(processName)s: %(message)s')


def worker1(d, lock):
    logging.debug('worker1 start')
    with lock:
        d['x'] += 1
        time.sleep(2)
        logging.debug(d)
    logging.debug('worker1 end')


def worker2(d, lock):
    logging.debug('worker2 start')
    with lock:
        d['x'] += 1
        time.sleep(2)
        logging.debug(d)
    logging.debug('worker2 end')


if __name__ == '__main__':
    # threadと異なりdは共有されない
    d = {'x': 0}
    lock = multiprocessing.Lock()
    p1 = multiprocessing.Process(target=worker1, args=(d, lock))
    p2 = multiprocessing.Process(target=worker2, args=(d, lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    logging.debug(d)
