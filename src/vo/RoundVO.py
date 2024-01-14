# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : RoundVO
# @Time   : 2024/1/14 13:32
# @Author : mango
from src.vo.ParamVO import ParamVO


class RoundVO(ParamVO):

    def __init__(self, left, right, separator, inputStr):
        self.left = left
        self.right = right
        self.separator = separator
        self.inputStr = inputStr
