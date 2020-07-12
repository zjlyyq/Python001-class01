from multiprocessing import Process, Value, Array, Lock
import time

def f(n, offset, lock):
    lock.acquire()  #加锁
    for _ in range(5):
        n.value += offset
        time.sleep(1)
        print(n.value)
    lock.release()  #释放

if __name__ == "__main__":
    share_num = Value('d', 0)
    lock = Lock()   #进程锁
    p1= Process(target=f, args=(share_num, 1, lock))
    p2= Process(target=f, args=(share_num, -1, lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()