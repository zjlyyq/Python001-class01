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

