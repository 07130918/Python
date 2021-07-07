import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1():
    logging.debug('start')
    time.sleep(1)
    logging.debug('end')


if __name__ == '__main__':
    # threads = []
    for _ in range(5):
        t1 = threading.Thread(target=worker1)
        t1.setDaemon(True)
        t1.start()
        # threads.append(t1)
    print(threading.enumerate())
    for thr in threading.enumerate():
        if thr is threading.current_thread():
            continue
        thr.join()
