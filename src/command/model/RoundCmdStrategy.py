# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : RoundCmdStrategy
# @Time   : 2023/12/31 13:54
# @Author : mango
from src.command.config.CmdTypeEnum import CmdTypeEnum
from src.command.model.CmdStrategy import CmdStrategy


class RoundCmdStrategy(CmdStrategy):
    def execute(self, app):
        args = app.argument.get_args()
        infile = args.in_file
        outfile = args.out_file
        separator = args.separator
        left = args.left
        right = args.right
        result = ""
        with open(infile, "r") as file:
            index = 1
            lines = file.readlines()
            rows = len(lines)
            for line in lines:
                line = line.replace("\n", "")
                result += left + line + right
                if index != rows:
                    result += separator
                index += 1
        with open(outfile, "w") as file:
            file.write(result)
        pass

    def register(self, subparsers):
        cmd = subparsers.add_parser('round', help='子命令round,切面命令')
        cmd.add_argument('-l', '--left', type=str, default="'", help='左侧字符，默认为%(default)s')
        cmd.add_argument('-r', '--right', type=str, default="'", help='右侧字符，默认为%(default)s')
        cmd.add_argument('-s', '--separator', type=str, default=",\n", help='分割字符，默认为%(default)s')
        cmd.add_argument('-i', '--in_file', type=str, default="input.txt", help='输入文件，默认为%(default)s')
        cmd.add_argument('-o', '--out_file', type=str, default="output.txt", help='输出文件，默认为%(default)s')
        pass

    def type(self):
        return CmdTypeEnum.FORMATE

