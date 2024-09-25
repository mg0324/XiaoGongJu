# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : Config
# @Time   : 2023/12/31 11:59
# @Author : mango


# 配置类
class Config:
    # 系统版本
    __version = "1.3.0"
    # 日志级别
    log_level = "debug"
    # 窗体大小
    windowSize = (1400, 800)
    # 关于
    about = {
        "name": "小工具",
        "version": __version,
        "copyright": "(C) 2024 MangoMei",
        "desc": "妙娃程序，专注于帮忙妙头运营店铺的自动化工具！"
    }

    def __init__(self):
        pass


