import logging
import queue
import threading

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1(queue):
    logging.debug('worker1 start')
    while True:
        item = queue.get()
        if item is None:
            break
        logging.debug(item)
        queue.task_done()

    logging.debug('--------------------------------')
    logging.debug('end')


if __name__ == '__main__':
    queue = queue.Queue()
    for i in range(1, 100001):
        queue.put(i)

    ts = []
    # 3本のthreadを走らせる
    for _ in range(3):
        t = threading.Thread(target=worker1, args=(queue, ))
        t.start()
        ts.append(t)

    logging.debug('tasks are not done')
    queue.join()
    logging.debug('tasks are done')
    print(ts)
    for _ in range(len(ts)):
        queue.put(None)
    [t.join() for t in ts]
