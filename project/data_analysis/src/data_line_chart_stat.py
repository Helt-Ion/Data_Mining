import os
import numpy as np
import pandas as pd
import time


def get_parquet_files(data_file, part_num):
	parquet_files = []
	for i in range(0, part_num):
		parquet_file = os.path.join(data_file, f"part-{i:05d}_items_info.parquet")
		parquet_files.append(parquet_file)
	return parquet_files


def data_tally(data_frame, by):
	return data_frame[by].value_counts().sort_index()


def update_stat(data_stat, data_frame):
	for row_id, purchase_date, item_id, price, categories in data_frame.values:
		data_stat.append([purchase_date, price])


def data_line_chart_stat_sub(data_file, part_num):
	price_stat = []
	goal_id = 1
	goal_category = '上衣'
	for ind, parquet_file in enumerate(get_parquet_files(data_file, part_num)):
		print(f"Reading {parquet_file}...")
		data = pd.read_parquet(parquet_file)
		print(data)
		filtered_data = data[(data['item_id'] == goal_id) & (data['categories'] == goal_category)]
		print(filtered_data)
		update_stat(price_stat, filtered_data)
		del data, filtered_data
	output_txt = os.path.join(data_file, "line_chart_stat.txt")
	with open(output_txt, "w", encoding='utf-8') as f:
		print(price_stat, file=f)
	print(f"Info saved to {output_txt}!")


def data_line_chart_stat():
	data_line_chart_stat_sub("data/10G_data_new", 8)
	data_line_chart_stat_sub("data/30G_data_new", 16)


def main():
	start_time = time.time()
	data_line_chart_stat()
	end_time = time.time()
	execution_time = end_time - start_time
	print(f"Execution time: {execution_time:.2f}s")


if __name__ == '__main__':
	main()
