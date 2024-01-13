# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : TemplateConfig
# @Time   : 2024/1/13 21:33
# @Author : mango

class TemplateConfig:

    @staticmethod
    def getConfig():
        return {
            "default": {
                "desc": "默认模板",
                "left": "'",
                "right": "'",
                "separator": ",\\n"
            },
            "result.add": {
                "desc": "代码集合添加模板",
                "left": "result.add(\"",
                "right": "\")",
                "separator": ";\\n"
            }
        }
