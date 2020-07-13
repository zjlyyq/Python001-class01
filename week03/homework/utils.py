import ping3
# from multiprocessing import Lock
import os

def ping_by_ping3(p_id, ip, lock):
    print(ip)
    r = ping3.ping(ip)
    lock.acquire()
    if r:
        print(f'进程号：{p_id}:{os.getpid()}，{ip} is arrival')
    else:
        print(f'进程号：{p_id}:{os.getpid()}，{ip} is not arrival')
    lock.release()