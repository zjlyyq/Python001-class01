import argparse
import pretty_errors
import ping3 
import ping3

r = ping3.ping('121.199.20.52')
print(r)
# parser cimmond ling argumnts
parser = argparse.ArgumentParser()
parser.add_argument('-f', default="tcp", nargs="?", choices=['ping', 'tcp'], help="protocol, tcp or ping[default]")
parser.add_argument('-n', type=int, default="4", nargs="?", help="the number of thread or process,dafault 4")
parser.add_argument('-ip', default="4", required=True, nargs="?", help="ip range e.g. 192.168.1.0-192.168.1.255 or a single ip address")
parser.add_argument('-w', default="result.json", nargs="?", help="result writen to a file")

argc = parser.parse_args()

