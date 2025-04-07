import os
import numpy as np
import pandas as pd
import time


def get_parquet_files(data_file, part_num):
	parquet_files = []
	for i in range(0, part_num):
		parquet_file = os.path.join(data_file, f"part-{i:05d}_purchase_history.parquet");
		parquet_files.append(parquet_file)
	return parquet_files


def data_tally(data_frame, by):
	return data_frame[by].value_counts().sort_index()


def data_purchase_history_stat_sub(data_file, part_num):
	for ind, parquet_file in enumerate(get_parquet_files(data_file, part_num)):
		print(f"Reading {parquet_file}...")
		data = pd.read_parquet(parquet_file)
		print(data)
		data_avg_price = data_tally(data, 'avg_price')
		print("Sort by avg_price:")
		print(data_avg_price)
		data_categories = data_tally(data, 'categories')
		print("Sort by categories:")
		print(data_categories)
		data_payment_method = data_tally(data, 'payment_method')
		print("Sort by payment_method:")
		print(data_payment_method)
		data_payment_status = data_tally(data, 'payment_status')
		print("Sort by payment_status:")
		print(data_payment_status)
		data_items_count = data_tally(data, 'items_count')
		print("Sort by items_count:")
		print(data_items_count)
		del data, data_avg_price, data_categories, data_payment_method, data_payment_status, data_items_count


def data_purchase_history_stat():
	data_purchase_history_stat_sub("data/10G_data_new", 1)


def main():
	start_time = time.time()
	data_purchase_history_stat()
	end_time = time.time()
	execution_time = end_time - start_time
	print(f"Execution time: {execution_time:.2f}s")


if __name__ == '__main__':
	main()
