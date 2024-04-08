# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : JSONCmdStrategy
# @Time   : 2023/12/31 22:43
# @Author : mango
from src.config.CmdTypeEnum import CmdTypeEnum
from src.model.future.json.JSONService import JSONService
from src.model.cmd.CmdStrategy import CmdStrategy
from src.vo.JSONVO import JSONVO


class JSONCmdStrategy(CmdStrategy):
    def __init__(self):
        self.service = JSONService()

    def execute(self, app):
        # 格式化json
        file = app.argument.get_args().file
        if file:
            with open(file, 'r') as f:
                data = f.read()
            # json格式化
            data = self.service.getResult(JSONVO(data))
            with open(file, 'w') as f:
                f.write(data)

    def register(self, subparsers):
        cmd = subparsers.add_parser('json', help='子命令json, json格式化命令')
        cmd.add_argument('-f', '--file', type=str, default="input.txt", help='待格式化文件，默认为%(default)s')

    def type(self):
        return CmdTypeEnum.FORMATE
