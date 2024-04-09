# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : Config
# @Time   : 2023/12/31 11:59
# @Author : mango


# 配置类
class Config:
    # 系统版本
    __version = "1.0.0"
    # 日志级别
    log_level = "debug"
    # 窗体大小
    windowSize = (1200, 800)
    # 关于
    about = {
        "name": "小工具",
        "version": "1.0.0",
        "copyright": "(C) 2024 MangoMei",
        "desc": "一个简单的工具箱"
    }

    def __init__(self):
        pass


