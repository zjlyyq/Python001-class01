import threading
import time
num = 0
mutex = threading.Lock()
def addone(n):
    global num
    if mutex.acquire(1):
        num += 1
        # time.sleep(1)  #  必须休眠，否则观察不到脏数据
        print(f'thread {n}: num value is {num}')
    mutex.release()

for i in range(5):
    t = threading.Thread(target = addone, args=(i,))
    t.start()

print('main thread stop')
