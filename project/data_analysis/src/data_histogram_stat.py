import os
import numpy as np
import pandas as pd
import time


def get_parquet_files(data_file, part_num):
	parquet_files = []
	for i in range(0, part_num):
		parquet_file = os.path.join(data_file, f"part-{i:05d}_login_history.parquet")
		parquet_files.append(parquet_file)
	return parquet_files


def data_tally(data_frame, by):
	return data_frame[by].value_counts().sort_index()


def update_stat(data_stat, data_frame):
	for index, count in data_frame.items():
		for i in range(0, count):
			data_stat.append(index)


def data_histogram_stat_sub(data_file, part_num):
	income_stat = []
	for ind, parquet_file in enumerate(get_parquet_files(data_file, part_num)):
		print(f"Reading {parquet_file}...")
		data = pd.read_parquet(parquet_file)
		print(data)
		data_income = data_tally(data, 'income')
		print(data_income)
		update_stat(income_stat, data_income)
		del data, data_income
	output_txt = os.path.join(data_file, "histogram_stat.txt")
	with open(output_txt, "w", encoding='utf-8') as f:
		print(income_stat, file=f)
	print(f"Info saved to {output_txt}!")


def data_histogram_stat():
	data_histogram_stat_sub("data/10G_data_new", 8)
	data_histogram_stat_sub("data/30G_data_new", 16)


def main():
	start_time = time.time()
	data_histogram_stat()
	end_time = time.time()
	execution_time = end_time - start_time
	print(f"Execution time: {execution_time:.2f}s")


if __name__ == '__main__':
	main()
