# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : RoundService
# @Time   : 2024/1/14 13:23
# @Author : mango
from src.model.Service import Service
from src.vo.RoundVO import RoundVO


class RoundService(Service):

    def getResult(self, roundVO: RoundVO):
        result = ""
        lines = roundVO.inputStr
        index = 1
        rows = len(lines)
        for line in lines:
            line = line.replace("\n", "")
            result += roundVO.left + line + roundVO.right
            if index != rows:
                result += roundVO.separator
            index += 1
        return result
