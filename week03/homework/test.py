import os
ret = os.system('ping -n 2 -w 3 121.199.20.52 > nul')
print(ret)