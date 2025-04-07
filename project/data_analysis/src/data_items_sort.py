import os
import numpy as np
import pandas as pd
import time


global_categories = ['上衣', '健身器材', '儿童课外读物', '内衣', '办公用品', '卫浴用品', '厨具', '围巾', '外套', \
'婴儿用品', '家具', '帽子', '平板电脑', '床上用品', '户外装备', '手套', '摄像机', '文具', '智能手机', '智能手表', \
'模型', '水产', '水果', '汽车装饰', '游戏机', '玩具', '益智玩具', '相机', '笔记本电脑', '米面', '耳机', '肉类', \
'蔬菜', '蛋奶', '裙子', '裤子', '调味品', '车载电子', '零食', '鞋子', '音响', '饮料']


def get_parquet_files(data_file, part_num):
	parquet_files = []
	for i in range(0, part_num):
		parquet_file = os.path.join(data_file, f"part-{i:05d}_items_info.parquet");
		parquet_files.append(parquet_file)
	return parquet_files


def data_sort(data_frame, by, items):
	ret = data_frame.sort_values(by=by, ascending=True)
	return ret.filter(items=items)


def data_items_sort_sub(data_file, part_num):
	for ind, parquet_file in enumerate(get_parquet_files(data_file, part_num)):
		print(f"Reading {parquet_file}...")
		data = pd.read_parquet(parquet_file)
		print(data)
		data_item_id = data_sort(data, 'item_id', ['item_id', 'price', 'categories', 'purchase_date', 'row_id'])
		print(data_item_id)
		for goal_id in range(1, 5):
			print("Filter by item_id:")
			print(f"Check item_id = {goal_id} and sort by purchase_date:")
			filtered_data = data[data['item_id'] == goal_id]
			items_purchase_date = data_sort(filtered_data, 'purchase_date', ['item_id', 'price', 'categories', 'purchase_date', 'row_id'])
			print(items_purchase_date)
			del filtered_data, items_purchase_date
			print("Filter by item_id and categories:")
			for goal_category in global_categories:
				print(f"Check item_id = {goal_id} and categories = {goal_category} and sort by purchase_date:")
				filtered_data = data[(data['item_id'] == goal_id) & (data['categories'] == goal_category)]
				items_purchase_date = data_sort(filtered_data, 'purchase_date', ['item_id', 'price', 'categories', 'purchase_date', 'row_id'])
				print(items_purchase_date)
				del filtered_data, items_purchase_date
		del data, data_item_id


def data_items_sort():
	data_items_sort_sub("data/10G_data_new", 1)


def main():
	start_time = time.time()
	data_items_sort()
	end_time = time.time()
	execution_time = end_time - start_time
	print(f"Execution time: {execution_time:.2f}s")


if __name__ == '__main__':
	main()
