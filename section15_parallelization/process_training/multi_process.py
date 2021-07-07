import logging
import multiprocessing
import time
from multiprocessing import (Array, Barrier, Condition, Event, Lock, Manager,
                             Pipe, Process, Queue, RLock, Semaphore, Value)

logging.basicConfig(level=logging.DEBUG, format='%(processName)s: %(message)s')


def worker1(i):
    logging.debug('worker1 start')
    logging.debug(i)
    time.sleep(3)
    logging.debug('worker1 end')


def worker2(i):
    logging.debug('worker2 start')
    logging.debug(i)
    logging.debug('worker2 end')


if __name__ == '__main__':
    i = 10
    p1 = multiprocessing.Process(target=worker1, args=(i, ))
    p1.daemon = True
    p2 = multiprocessing.Process(
        name='rename worker2', target=worker2, args=(i, ))
    p1.start()
    p2.start()
    p1.join()
