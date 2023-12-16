# XiaoGongJu
小工具积累

## 环境安装
安装`python3.6`后执行安装依赖命令。
``` shell
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 架构设计

## 目录结构
* src - 项目源码
* dist - 打包后的代码
* doc - 文档

## 打包发布
``` shell
pip install pyinstaller
pyinstaller -F src/app.py
```

