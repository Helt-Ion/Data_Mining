import os
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


def main():
	# 设置字体，确保中文显示正常(非必须添加此代码)
	matplotlib.rcParams['font.sans-serif'] = ['SimHei']
	
	# 扇形图配色
	color_palette = ['#FF9AA2', '#FFB7B2', '#FFDAC1', '#E2F0CB', '#B5EAD7', '#C7CEEA', '#F8B195', '#F67280', '#6C5B7B', '#355C7D']

	# 原始数据
	data_10GB = {'中国': 4498337, '俄罗斯': 4499132, '印度': 4499562, '巴西': 4500526, '德国': 4500370, '日本': 4498695, '法国': 4501427, '澳大利亚': 4499124, '美国': 4501158, '英国': 4501669}
	data_30GB = {'中国': 13498904, '俄罗斯': 13500996, '印度': 13502855, '巴西': 13498665, '德国': 13496833, '日本': 13498944, '法国': 13499078, '澳大利亚': 13502953, '美国': 13502589, '英国': 13498183}

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
	plt.savefig("pie_chart_country.png")
	plt.show()


if __name__ == '__main__':
	main()
