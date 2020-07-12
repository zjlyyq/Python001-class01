
import pretty_errors
from multiprocessing import Process, Queue
import time

def run(q):
    time.sleep(1)
    q.put([42, None, 'hello'])

if __name__ == "__main__":
    q = Queue()
    p = Process(target=run, args=(q,))
    p.start()
    # 阻塞1秒，一秒拿不到值说明是队列是空的，raise Empty
    print(q.get(block=True, timeout=2))
    p.join()

