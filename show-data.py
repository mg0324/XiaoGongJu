# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: miaowa
# @File   : show-data
# @Time   : 2024/6/12 23:33
# @Author : mango

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 设置中文字体
font = FontProperties(fname='/System/Library/Fonts/STHeiti Light.ttc')  # macOS系统的示例路径

# 读取Excel文件中的数据
file_path = 'sport_data.xlsx'

# 使用pandas读取Excel数据
df = pd.read_excel(file_path, engine='openpyxl')

# 将日期列转换为datetime类型
df['日期'] = pd.to_datetime(df['日期'])

# 将评分列转换为浮点数
df['评分'] = df['评分'].str.rstrip('%').astype('float')

# 绘制评分折线图
plt.figure(figsize=(12, 6))
plt.plot(df['日期'], df['评分'], marker='o', linestyle='-', color='b', label='评分')

# 绘制follower折线图
plt.plot(df['日期'], df['follower'], marker='x', linestyle='--', color='g', label='Follower')

# 添加标题和标签
plt.title(file_path + ' 评分和关注者随时间变化图', fontproperties=font)
plt.xlabel('日期', fontproperties=font)
plt.ylabel('值', fontproperties=font)

# 显示图例
plt.legend(prop=font)

# 显示网格
plt.grid(True)

# 显示图表
plt.show()
