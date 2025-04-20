import os
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


def main():
	# 设置字体，确保中文显示正常(非必须添加此代码)
	matplotlib.rcParams['font.sans-serif'] = ['SimHei']
	
	# 扇形图配色
	color_palette = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

	# 原始数据
	data_10GB = {'其他': 898865, '女': 21598086, '未指定': 899652, '男': 21603397}
	data_30GB = {'其他': 2698372, '女': 64792563, '未指定': 2698564, '男': 64810501}

	# 处理后的数据
	data_left = data_10GB.values()     # 左侧数据
	data_right = data_30GB.values()    # 右侧数据
	data_labels = data_10GB.keys()     # 数据标签

	# 创建画布和子图
	fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

	# 绘制左侧饼图
	ax1.pie(data_left, 
			labels=data_labels, 
			autopct='%1.1f%%', 
			startangle=90,
			colors=color_palette)
	ax1.set_title('10GB数据', fontsize=14, fontweight='bold')

	# 绘制右侧饼图
	ax2.pie(data_right,
			labels=data_labels,
			autopct='%1.1f%%',
			startangle=90,
			colors=color_palette)
	ax2.set_title('30GB数据', fontsize=14, fontweight='bold')

	# 调整布局
	plt.tight_layout(pad=3)  # 增加子图间距
	plt.savefig("pie_chart_gender.png")
	plt.show()


if __name__ == '__main__':
	main()
