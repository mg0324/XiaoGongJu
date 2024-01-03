# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : JSONCmdStrategy
# @Time   : 2023/12/31 22:43
# @Author : mango
import json

from src.config.CmdTypeEnum import CmdTypeEnum
from src.model.CmdStrategy import CmdStrategy


class JSONCmdStrategy(CmdStrategy):
    def execute(self, app):
        # 格式化json
        file = app.argument.get_args().file
        if file:
            with open(file, 'r') as f:
                data = f.read()
            # json格式化
            data = json.loads(data)
            data = json.dumps(data, indent=4, ensure_ascii=False)
            with open(file, 'w') as f:
                f.write(data)

    def register(self, subparsers):
        cmd = subparsers.add_parser('json', help='子命令json, json格式化命令')
        cmd.add_argument('-f', '--file', type=str, default="input.txt", help='待格式化文件，默认为%(default)s')

    def type(self):
        return CmdTypeEnum.FORMATE
