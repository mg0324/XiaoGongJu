# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : Singleton
# @Time   : 2024/1/28 13:00
# @Author : mango

from abc import ABC, abstractmethod


# 单例模式
class Singleton(ABC):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    @abstractmethod
    def getInstance(self):
        pass

