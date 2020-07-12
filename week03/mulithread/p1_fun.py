import threading
import os
def f(n):
    print(f'当前线程的进程：{os.getpid()}, ' + n)

if __name__ == "__main__":
    thread1 = threading.Thread(target=f, args=('thread1',))
    thread1.start()
    thread1.join() 
    print(f'主进程：{os.getpid()} 结束')