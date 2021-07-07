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
    with multiprocessing.Pool(2) as p:
        r = p.map_async(worker1, [100, 200])
        logging.debug('executed')
        logging.debug(r.get())

        r = p.imap(worker1, [100, 200, 300])
        logging.debug('execute imap')
        logging.debug([i for i in r])
