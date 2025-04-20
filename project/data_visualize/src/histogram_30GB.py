import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json


def main():
	# 设置字体，确保中文显示正常(非必须添加此代码)
	plt.rcParams['font.sans-serif'] = ['SimHei']
	plt.rcParams['axes.unicode_minus'] = False

	# 示例数据
	with open('data/30G_data_new/histogram_stat.txt', 'r') as f:
		data = json.load(f)

	# 创建直方图
	plt.figure(figsize=(10, 6))
	plt.hist(data, bins=range(0, 1000000, 10000), color='#4C72B0', edgecolor='black', density=True)

	# 设置图表标题和坐标轴标签
	plt.title('频率分布直方图_30GB数据', fontsize=14, pad=20)
	plt.xlabel('用户收入', fontsize=12)
	plt.ylabel('频率', fontsize=12)

	# 禁用科学计数法
	plt.gcf().axes[0].xaxis.get_major_formatter().set_scientific(False)

	plt.tight_layout()
	plt.savefig("histogram_30GB.png")
	plt.show()


if __name__ == '__main__':
	main()
