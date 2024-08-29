# coding=utf-8
import time
from functools import wraps
from src.model.future.miaowa.compontent.LogUtil import LogUtil


# 装饰器注解GetTime
# @GetTime
def GetTime(stage):
    def doit(func):
        @wraps(func)
        def inner(*args, **kwarg):
            s1 = time.perf_counter()
            res = func(*args, **kwarg)
            e1 = time.perf_counter()
            prefix = ""
            if len(stage) > 0:
                prefix = "["+stage+"]"
            LogUtil.info(prefix + "用时" + str(int(e1) - int(s1)) + "秒")
            return res
        return inner
    return doit

