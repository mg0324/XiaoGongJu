# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : CmdEnum
# @Time   : 2023/12/31 15:31
# @Author : mango
from enum import Enum


class CmdEnum(Enum):
    ROUND = {
        "value": "round",
        "desc": "切面命令，在字符串前后可以新增自定义内容。"
    }
    JSON = {
        "value": "json",
        "desc": "json格式化命令，可以将字符串格式化为json格式。"
    }

    @staticmethod
    def getItemByValue(value):
        for item in CmdEnum:
            if item.value.get("value") == value:
                return item
        return ""

