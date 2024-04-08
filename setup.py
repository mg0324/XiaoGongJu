# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : setup
# @Time   : 2024/1/28 11:48
# @Author : mango

from setuptools import setup

setup(
    name='xiaoGongju',
    version='0.1',
    description='A description of your package',
    author='mangomei',
    author_email='1092017732@qq.com',
    packages=['src/model'],
    install_requires=[
        'wxPython'
    ],
)
