import os
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import ast
from matplotlib.dates import DateFormatter
from datetime import datetime


def main():
	# 设置字体，确保中文显示正常(非必须添加此代码)
	matplotlib.rcParams['font.sans-serif'] = ['SimHei']

	# 原始数据
	with open('data/10G_data_new/line_chart_stat.txt', 'r') as f:
		content = f.read()
		data = ast.literal_eval(content)

	# 数据预处理：转换日期格式并排序
	sorted_data = sorted(data, key=lambda x: datetime.strptime(x[0], '%Y-%m-%d'))
	dates = [datetime.strptime(item[0], '%Y-%m-%d') for item in sorted_data]
	prices = [item[1] for item in sorted_data]

	# 创建图表
	plt.figure(figsize=(12, 6))

	# 绘制折线图
	plt.plot(dates, prices, linestyle='-', color='blue', linewidth=2)

	# 设置标题和标签
	plt.title('价格随时间的变化趋势', fontsize=14, fontweight='bold')
	plt.xlabel('日期', fontsize=12)
	plt.ylabel('价格', fontsize=12)

	# 设置日期格式
	date_format = DateFormatter('%Y-%m-%d')
	plt.gca().xaxis.set_major_formatter(date_format)

	# 添加网格和调整布局
	plt.grid(True, linestyle='--', alpha=0.7)
	plt.tight_layout()

	# 显示图表
	plt.savefig("line_chart.png")
	plt.show()


if __name__ == '__main__':
	main()
