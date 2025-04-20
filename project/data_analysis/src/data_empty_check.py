import os
import numpy as np
import pandas as pd
import time
	

def get_nulls(data_frame):
	return data_frame[data_frame.isnull().any(axis=1)]


def parquet_empty_check(data_file, part_num):
	parquet_files = []
	for i in range(0, part_num):
		parquet_file = os.path.join(data_file, f"part-{i:05d}.parquet")
		parquet_files.append(parquet_file)
	for file in parquet_files:
		print(f"Reading {file}...")
		data_frame = pd.read_parquet(file)
		data_null = get_nulls(data_frame)
		print(data_null)


def data_empty_check():
	print("Parquet empty check...")
	parquet_empty_check("data/10G_data_new", 8)
	parquet_empty_check("data/30G_data_new", 16)


def main():
	start_time = time.time()
	data_empty_check()
	end_time = time.time()
	execution_time = end_time - start_time
	print(f"Execution time: {execution_time:.2f}s")


if __name__ == '__main__':
	main()
