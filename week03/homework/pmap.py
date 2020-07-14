import argparse
import pretty_errors
import ping3
from multiprocessing import Process, Queue, Lock
from multiprocessing.pool import Pool
import os
import random
import time
import subprocess
# from utils import ping_by_ping3

# parser cimmond ling argumnts
parser = argparse.ArgumentParser()
parser.add_argument('-f', default="tcp", nargs="?", choices=['ping', 'tcp'], help="protocol, tcp or ping[default]")
parser.add_argument('-n', type=int, default="4", nargs="?", help="the number of thread or process,dafault 4")
parser.add_argument('-ip', default="4", required=True, nargs="?", help="ip range e.g. 192.168.1.0-192.168.1.255 or a single ip address")
parser.add_argument('-w', default="result.json", nargs="?", help="result writen to a file")

# ip, ip_status, lock
def ping_by_ping3(t):
    print(f'进程{t[0]}开始，ip = {t[1]} 进程号：{os.getpid()}')
    r = ping3.ping(t[1])
    print(f'进程{t[1]}结束， 进程号：{os.getpid()}')
    if r:
        return {t[1]: 'arrival'}
    else:
        return {t[1]: 'not arrival'}
if __name__ == "__main__": 
    argc = parser.parse_args()
    ip_range = argc.ip.split('-')
    op_type = argc.f
    p = Pool(4)
    lock = Lock()
    process_id = 0
    plist = []
    ip_status = Queue()
    ip_list = []
    for ip1 in range(int(ip_range[0].split('.')[0]), int(ip_range[1].split('.')[0])+1):
        for ip2 in range(int(ip_range[0].split('.')[1]), int(ip_range[1].split('.')[1])+1):
            for ip3 in range(int(ip_range[0].split('.')[2]), int(ip_range[1].split('.')[2])+1):
                for ip4 in range(int(ip_range[0].split('.')[3]), int(ip_range[1].split('.')[3])+1):
                    cur_ip = str(ip1) + '.' + str(ip2) + '.' + str(ip3) + '.' + str(ip4)
                    process_id += 1
                    ip_list.append((process_id,cur_ip))
    result = p.map(ping_by_ping3, ip_list)
    print(type(result))
    p.close()
    p.join()
    p.terminate()
    print(result)
    print('父进程结束.')

