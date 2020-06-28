Scrapy学习笔记

安装

`pip install scrapy`

基本用法

```bash
Usage:
  scrapy <command> [options] [args]

Available commands:
  bench         Run quick benchmark test
  commands      
  fetch         Fetch a URL using the Scrapy downloader
  genspider     Generate new spider using pre-defined templates
  runspider     Run a self-contained spider (without creating a project)
  settings      Get settings values
  shell         Interactive scraping console
  startproject  Create new project
  version       Print Scrapy version
  view          Open URL in browser, as seen by Scrapy

  [ more ]      More commands available when run from project directory

Use "scrapy <command> -h" to see more info about a command
```

创建项目

`scrapy startproject project_name`

```bash
JialudeMacBook-Pro:week01 jialuzhang$ scrapy startproject first_scrapy_project
New Scrapy project 'first_scrapy_project', using template directory '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/scrapy/templates/project', created in:
    /Users/jialuzhang/MyCode/Python001-class01/week01/first_scrapy_project

You can start your first spider with:
    cd first_scrapy_project
    scrapy genspider example example.com
```

初始化一个爬虫

`cd first_scrapy_project`

`scrapy genspider example example.com`

目录结构如下

```bash
first_scrapy_project/
├── first_scrapy_project
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   └── settings.cpython-38.pyc
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py           # 设置保持位置
│   ├── settings.py            # 项目设置文件
│   └── spiders   
│       ├── __init__.py
│       ├── __pycache__
│       │   └── __init__.cpython-38.pyc
│       └── movies.py          # 爬虫逻辑
└── scrapy.cfg                 # 项目配置结构
```

启动爬虫

`scrapy crawl example.py`

