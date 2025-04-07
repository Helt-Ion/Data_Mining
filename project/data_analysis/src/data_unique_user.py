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


def data_unique_user():
	parquet_file = "data/30G_data_new/part-00000.parquet"
	print(f"Reading {parquet_file}...")
	data = pd.read_parquet(parquet_file)
	print(data)
	# Three terms
	data_unique_user = data_group(data, ['user_name', 'email', 'phone_number'], ['id'])
	print("Unique user:")
	print(data_unique_user)
	# Two terms
	data_user_name_email = data_group(data, ['user_name', 'email'], ['id'])
	print("Group by user_name and email:")
	print(data_user_name_email)
	data_user_name_phone_number = data_group(data, ['user_name', 'phone_number'], ['id'])
	print("Group by user_name and phone_number:")
	print(data_user_name_phone_number)
	data_email_phone_number = data_group(data, ['email', 'phone_number'], ['id'])
	print("Group by email and phone_number:")
	print(data_email_phone_number)


def main():
	start_time = time.time()
	data_unique_user()
	end_time = time.time()
	execution_time = end_time - start_time
	print(f"Execution time: {execution_time:.2f}s")


if __name__ == '__main__':
	main()
