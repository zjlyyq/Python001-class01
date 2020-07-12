from multiprocessing import Process, Value, Array
import time


def f(n, offset):
    for _ in range(5):
        n.value += offset
        time.sleep(1)
        print(n.value)


if __name__ == "__main__":
    share_num = Value('d', 0)
    p1= Process(target=f, args=(share_num, 1))
    p2= Process(target=f, args=(share_num, -1))
    p1.start()
    p2.start()
    p1.join()
    p2.join()