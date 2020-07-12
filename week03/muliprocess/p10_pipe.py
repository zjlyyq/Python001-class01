from multiprocessing import Process, Pipe
import pretty_errors
import os
def f(conn: Pipe):
    conn.send([42, None, 'hello'])
    conn.close()
    print(f'子进程：{os.getpid()}结束，父进程是：{os.getppid()}');

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()
    print(f'父进程：{os.getpid()}结束')