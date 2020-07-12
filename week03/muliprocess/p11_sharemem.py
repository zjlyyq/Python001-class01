from multiprocessing import Process, Value, Array
import time


def f(n, a):
    n.value = 3.1415926
    for i in a:
        a[i] = -a[i]


if __name__ == "__main__":
    num, arr = Value('d', 0.0), Array('i', range(10))
    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])