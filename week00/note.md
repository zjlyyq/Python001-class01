### 环境搭建篇——磨刀不误砍柴工

#### python多版本共存

直接安装，但是具体使用要看哪个版本在`enveriment path`中靠前。

#### pip包管理工具

1. python3.x(具体忘记了)之后自带pip。

2. 配置pip源，加快第三方库安装速度

   ```bash
   豆瓣： https://pypi.doubanio.com/simple/
   清华： https://mirrors.tuna.tsinghua.edu.cn/help/pypi/
   中科大： https://pypi.mirrors.ustc.edu.cn/simple/
   阿里云： https://mirrors.aliyun.com/pypi/simple/
   ```

   + 临时替换
     + `pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package`
   + 永久替换
     + `pip config set global.index-url https://pypi.mirrors.ustc.edu.cn/simple/ `

3. 环境迁移 pip freeze

   ```bash
   # A 机器
   pip freeze requirements.txt
   
   # B 机器
   pip install -r requirements.txt
   ```

#### venv虚拟环境配置

+ 新建虚拟环境

  ```bash
  python3 -m venv venv2
  ```

+ 进入虚拟环境

  ```bash
  ➜  MyCode source venv1/bin/activate
  (venv1) ➜  MyCode
  ```

  ![](/Users/jialuzhang/MyCode/Python001-class01/week00/截屏2020-06-21 21.09.46.png)

### python 基本语法

- Python 标准语法：[ https://docs.python.org/zh-cn/3.7/tutorial/index.html](https://docs.python.org/zh-cn/3.7/tutorial/index.html)
- Python 内置函数：[ https://docs.python.org/zh-cn/3.7/library/functions.html](https://docs.python.org/zh-cn/3.7/library/functions.html)
- Python 内置类型：[ https://docs.python.org/zh-cn/3.7/library/stdtypes.html](https://docs.python.org/zh-cn/3.7/library/stdtypes.html)
- Python 数据类型：[ https://docs.python.org/zh-cn/3.7/library/datatypes.html](https://docs.python.org/zh-cn/3.7/library/datatypes.html)
- Python 标准库：[ https://docs.python.org/zh-cn/3.7/library/index.html](https://docs.python.org/zh-cn/3.7/library/index.html)
- Python 计算器使用：[ https://docs.python.org/zh-cn/3.7/tutorial/introduction.html](https://docs.python.org/zh-cn/3.7/tutorial/introduction.html)
- Python 数据结构：[ https://docs.python.org/zh-cn/3.7/tutorial/datastructures.html](https://docs.python.org/zh-cn/3.7/tutorial/datastructures.html)
- Python 其他流程控制工具 :[ https://docs.python.org/zh-cn/3.7/tutorial/controlflow.html](https://docs.python.org/zh-cn/3.7/tutorial/controlflow.html)
- Python 中的类：[ https://docs.python.org/zh-cn/3.7/tutorial/classes.html](https://docs.python.org/zh-cn/3.7/tutorial/classes.html)
- Python 定义函数：[ https://docs.python.org/zh-cn/3.7/tutorial/controlflow.html#defining-functions](https://docs.python.org/zh-cn/3.7/tutorial/controlflow.html#defining-functions)

> python交互式shell下，可以连按两下 `tab` 键补全
>
> 元祖相比列表是不可变的，因此可以作为字典的key，也可以存入集合。