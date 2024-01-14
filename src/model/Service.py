# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : Service
# @Time   : 2024/1/14 13:26
# @Author : mango
from abc import ABC, abstractmethod
from src.vo.ParamVO import ParamVO


class Service(ABC):

    @abstractmethod
    def getResult(self, paramVO: ParamVO):
        pass

