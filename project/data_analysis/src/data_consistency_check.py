import os
import numpy as np
import pandas as pd
import time


def data_group(data_frame, by, items):
	ret = data_frame.groupby(by).first()
	return ret.filter(items=items)


def find_duplicate_column(data_frame, by, items):
	ret = data_frame[data_frame.duplicated(subset=by, keep=False)]
	ret = ret.sort_values(by=by, ascending=True)
	return ret.filter(items=items)


def data_consistency_check():
	parquet_file = "data/10G_data_new/part-00000.parquet"
	print(f"Reading {parquet_file}...")
	data = pd.read_parquet(parquet_file)
	print(data)
	data_user_name = data_group(data, 'user_name', ['email', 'phone_number', 'id'])
	print("data_user_name:")
	print(data_user_name)
	data_phone_number = data_group(data, 'phone_number', ['user_name', 'email', 'id'])
	print("data_phone_number:")
	print(data_phone_number)
	data_email = data_group(data, 'email', ['user_name', 'phone_number', 'id'])
	print("data_email:")
	print(data_email)
	# Find all users with duplication
	data_user_name_dulplicated = find_duplicate_column(data, 'user_name', ['user_name', 'email', 'phone_number'])
	print("data_user_name_dulplicated:")
	print(data_user_name_dulplicated)
	# Find all emails with duplication
	data_email_dulplicated = find_duplicate_column(data, 'email', ['user_name', 'email', 'phone_number'])
	print("data_email_dulplicated:")
	print(data_email_dulplicated)


def main():
	start_time = time.time()
	data_consistency_check()
	end_time = time.time()
	execution_time = end_time - start_time
	print(f"Execution time: {execution_time:.2f}s")


if __name__ == '__main__':
	main()
