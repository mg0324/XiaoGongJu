# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : RoundCmdStrategy
# @Time   : 2023/12/31 13:54
# @Author : mango
from src.config.CmdTypeEnum import CmdTypeEnum
from src.model.RoundService import RoundService
from src.model.cmd.CmdStrategy import CmdStrategy
from src.vo.RoundVO import RoundVO


class RoundCmdStrategy(CmdStrategy):
    def __init__(self):
        self.service = RoundService()

    def execute(self, app):
        args = app.argument.get_args()
        infile = args.in_file
        outfile = args.out_file
        with open(infile, "r") as file:
            lines = file.readlines()
        roundVO = RoundVO(args.left, args.right, args.separator, lines)
        result = self.service.getResult(roundVO)
        with open(outfile, "w") as file:
            file.write(result)

    def register(self, subparsers):
        cmd = subparsers.add_parser('round', help='子命令round, 格式化命令')
        cmd.add_argument('-l', '--left', type=str, default="'", help='左侧字符，默认为%(default)s')
        cmd.add_argument('-r', '--right', type=str, default="'", help='右侧字符，默认为%(default)s')
        cmd.add_argument('-s', '--separator', type=str, default=",\n", help='分割字符，默认为%(default)s')
        cmd.add_argument('-i', '--in_file', type=str, default="input.txt", help='输入文件，默认为%(default)s')
        cmd.add_argument('-o', '--out_file', type=str, default="output.txt", help='输出文件，默认为%(default)s')

    def type(self):
        return CmdTypeEnum.FORMATE

