# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : JSONService
# @Time   : 2024/1/14 13:23
# @Author : mango
import json
from src.model.Service import Service
from src.vo.JSONVO import JSONVO


class JSONService(Service):

    def getResult(self, jsonVO: JSONVO):
        # json格式化
        try:
            data = json.loads(jsonVO.inputStr)
        except Exception as e:
            return "JSON格式化失败，错误信息：{}".format(e)
        return json.dumps(data, indent=4, ensure_ascii=False)
