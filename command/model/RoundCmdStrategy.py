# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : RoundCmdStrategy
# @Time   : 2023/12/31 13:54
# @Author : mango
from command.model.CmdStrategy import CmdStrategy


class RoundCmdStrategy(CmdStrategy):
    def execute(self, app):
        pass

    def register(self, subparsers):
        parser_round_cmd = subparsers.add_parser('round', help='子命令round,切面命令')
        pass

    def type(self):
        pass

