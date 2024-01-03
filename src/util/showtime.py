# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : ShowTime
# @Time   : 2023/12/31 11:26
# @Author : mango


import time
from functools import wraps
from src.util.LogUtil import LogUtil


# 装饰器注解getTime
# @showtime
def showtime(stage):
    def doit(func):
        @wraps(func)
        def inner(*args, **kwarg):
            s1 = time.time()
            res = func(*args, **kwarg)
            e1 = time.time()
            prefix = ""
            if len(stage) > 0:
                prefix = "[" + stage + "]"
            LogUtil.info(prefix + "用时" + str(int(e1) - int(s1)) + "秒")
            return res
        return inner
    return doit
