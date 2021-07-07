import logging
import multiprocessing
import time

logging.basicConfig(level=logging.DEBUG, format='%(processName)s: %(message)s')


def worker1(i):
    logging.debug('worker1 start')
    time.sleep(3)
    logging.debug('worker1 end')
    return i


if __name__ == '__main__':
    # poolで走らせるprocessの数を決める
    with multiprocessing.Pool(2) as p:
        # 同期
        logging.debug(p.apply(worker1, (200, )))
        logging.debug('executed apply')
        # 非同期
        p1 = p.apply_async(worker1, (100, ))
        p2 = p.apply_async(worker1, (100, ))
        p3 = p.apply_async(worker1, (100, ))
        logging.debug('executed')
        logging.debug(p1.get())
        logging.debug(p2.get())
        logging.debug(p3.get())
