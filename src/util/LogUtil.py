# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : LogUtil
# @Time   : 2023/12/31 11:23
# @Author : mango


# 控制台日志工具
class LogUtil:
    # 日志级别 error > info > debug > warning
    __level = "debug"
    # 分值
    __value = {
        "warning": 1,
        "debug": 2,
        "info": 3,
        "error": 4
    }

    @staticmethod
    def __level_value__():
        return LogUtil.__value.get(LogUtil.__level)

    @staticmethod
    def __log__(level, msg):
        if LogUtil.__value.get(level) >= LogUtil.__level_value__():
            print(msg)
        pass

    @staticmethod
    def set_level(level):
        LogUtil.__level = level
        pass

    @staticmethod
    def info(msg):
        LogUtil.__log__("info", msg)
        pass

    @staticmethod
    def debug(msg):
        LogUtil.__log__("debug", msg)
        pass

    @staticmethod
    def warning(msg):
        LogUtil.__log__("warning", msg)
        pass

    @staticmethod
    def error(msg):
        LogUtil.__log__("error", msg)
        pass

