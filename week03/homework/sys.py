import sys
import pretty_errors

def add(a, b):
    print(f'{a} + {b} = {int(a)+int(b)}')

if sys.argv[2]:
    a, b = sys.argv[1], sys.argv[2]
    try:
        add1 = int(a)
        add2 = int(b)
        add(a, b)
    except Exception as identifier:
        print('请输入数字作为参数！')
        # raise Exception('请输入数字作为参数！')

