import os
import numpy as np
import pandas as pd
import json
import time


def get_parquet_files(data_file, part_num):
	parquet_files = []
	for i in range(0, part_num):
		parquet_file = os.path.join(data_file, f"part-{i:05d}_purchase_history.parquet")
		parquet_files.append(parquet_file)
	return parquet_files


def data_purchase_history_items_sub(data_file, part_num):
	for ind, parquet_file in enumerate(get_parquet_files(data_file, part_num)):
		print(f"Reading {parquet_file}...")
		data = pd.read_parquet(parquet_file)
		print(data)
		data_items = data.filter(items=['id', 'purchase_date', 'avg_price', 'categories', 'items'])
		print(data_items)
		items_list = []
		for row_id, purchase_date, price, categories, items in data_items.values:
			for item_id in items:
				items_list.append([row_id, purchase_date, item_id, price, categories])
		result = pd.DataFrame(items_list, columns=['row_id', 'purchase_date', 'item_id', 'price', 'categories'])
		print(result)
		parquet_output = os.path.join(data_file, f"part-{ind:05d}_items_info.parquet");
		result.to_parquet(parquet_output)
		print(f"Converted data saved to {parquet_output}!")
		del data, data_items, result


def data_purchase_history_items():
	data_purchase_history_items_sub("data/10G_data_new", 8)
	data_purchase_history_items_sub("data/30G_data_new", 16)


def main():
	start_time = time.time()
	data_purchase_history_items()
	end_time = time.time()
	execution_time = end_time - start_time
	print(f"Execution time: {execution_time:.2f}s")


if __name__ == '__main__':
	main()
