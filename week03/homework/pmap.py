import argparse
import pretty_errors
import ping3
from multiprocessing import Process, Queue, Lock
from multiprocessing.pool import Pool
import os
# from utils import ping_by_ping3

# parser cimmond ling argumnts
parser = argparse.ArgumentParser()
parser.add_argument('-f', default="tcp", nargs="?", choices=['ping', 'tcp'], help="protocol, tcp or ping[default]")
parser.add_argument('-n', type=int, default="4", nargs="?", help="the number of thread or process,dafault 4")
parser.add_argument('-ip', default="4", required=True, nargs="?", help="ip range e.g. 192.168.1.0-192.168.1.255 or a single ip address")
parser.add_argument('-w', default="result.json", nargs="?", help="result writen to a file")


def run(name):
    print("%s子进程开始，进程ID：%d" % (name, os.getpid()))
    start = time()
    sleep(random.choice([1, 2, 3, 4]))
    end = time()
    print("%s子进程结束，进程ID：%d。耗时%0.2f" % (name, os.getpid(), end-start))

# ip, ip_status, lock
def ping_by_ping3(t):
    print(f'进程{t[0]}开始， 进程号：{os.getpid()}')
    # r = ping3.ping(ip)
    # lock.acquire()
    # if r:
    #     ip_status.put({ip: "arrival"})
    # else:
    #     ip_status.put({ip: "not arrival"})
    # lock.release()
    print(f'进程{t[0]}结束， 进程号：{os.getpid()}')

if __name__ == "__main__": 
    argc = parser.parse_args()
    ip_range = argc.ip.split('-')
    op_type = argc.f
    print(ip_range, op_type)
    p = Pool(2)
    print(p)
    lock = Lock()
    process_id = 0
    plist = []
    ip_status = Queue()
    for ip1 in range(int(ip_range[0].split('.')[0]), int(ip_range[1].split('.')[0])+1):
        for ip2 in range(int(ip_range[0].split('.')[1]), int(ip_range[1].split('.')[1])+1):
            for ip3 in range(int(ip_range[0].split('.')[2]), int(ip_range[1].split('.')[2])+1):
                for ip4 in range(int(ip_range[0].split('.')[3]), int(ip_range[1].split('.')[3])+1):
                    cur_ip = str(ip1) + '.' + str(ip2) + '.' + str(ip3) + '.' + str(ip4)
                    print(cur_ip)
                    process_id += 1
                    # p.apply_async(run, args=(process_id,))
                    # plist.append(Process(target=ping_by_ping3, args=(process_id, cur_ip, ip_status, lock)))
                    p.apply_async(ping_by_ping3, args=((process_id, cur_ip, ip_status ,lock, )))
                    # plist[process_id-1].start()
                    # plist[process_id-1].join()
    print('hhh')
    p.close()
    print('hhh2')
    p.join()
    print('hhh3')
    # p.terminate()
    print('hhh4')
    result = ip_status.get(timeout=3)
    print('hhh5')
    while result:
        print(result)
        try:
            result = ip_status.get(timeout=2)
        except Exception:
            break
    print('父进程结束.')

