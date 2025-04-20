import os
import numpy as np
import pandas as pd
import time


def get_parquet_files(data_file, part_num):
	parquet_files = []
	for i in range(0, part_num):
		parquet_file = os.path.join(data_file, f"part-{i:05d}.parquet")
		parquet_files.append(parquet_file)
	return parquet_files


def data_tally(data_frame, by):
	return data_frame[by].value_counts().sort_index()


def data_anomaly_check_val_sub(data_file, part_num):
	for parquet_file in get_parquet_files(data_file, part_num):
		print(f"Reading {parquet_file}...")
		data = pd.read_parquet(parquet_file)
		print(data)
		data_ages = data_tally(data, 'age')
		print("Sort by ages:")
		print(data_ages)
		data_income = data_tally(data, 'income')
		print("Sort by income:")
		print(data_income)
		data_last_login = data_tally(data, 'last_login')
		print("Sort by last_login:")
		print(data_last_login)
		data_registration_date = data_tally(data, 'registration_date')
		print("Sort by registration_date:")
		print(data_registration_date)


def data_anomaly_check_val():
	data_anomaly_check_val_sub("data/10G_data_new", 8)
	data_anomaly_check_val_sub("data/30G_data_new", 16)


def main():
	start_time = time.time()
	data_anomaly_check_val()
	end_time = time.time()
	execution_time = end_time - start_time
	print(f"Execution time: {execution_time:.2f}s")


if __name__ == '__main__':
	main()
