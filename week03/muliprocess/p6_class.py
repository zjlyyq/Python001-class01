from multiprocessing import Process
import pretty_errors
import time
import os

class CustomProcess(Process):
    
    def __init__(self, num):
        self.num = num
        super().__init__()

    def run(self):
        while True:
            print(f'我是进程{self.num}，我的pid是：{os.getpid()}')
            time.sleep(1)
    
for i in range(2):
    p = CustomProcess(i+1)
    p.start()
    time.sleep(3)
    p.terminate()
    p.join()

    