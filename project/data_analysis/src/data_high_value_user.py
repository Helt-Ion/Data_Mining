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


def data_high_value_user_sub(data_file, part_num):
	high_value_user = pd.DataFrame()
	select_num = 20
	for ind, parquet_file in enumerate(get_parquet_files(data_file, part_num)):
		print(f"Reading {parquet_file}...")
		data = pd.read_parquet(parquet_file)
		print(data)
		sorted_data = data[data['is_active'] == True]\
			.filter(items=['user_name', 'email', 'income', 'avg_price', 'login_count', 'avg_session_duration'])\
			.sort_values(by=['income', 'avg_price', 'login_count', 'avg_session_duration'], ascending=[False, False, False, False])
		print(sorted_data)
		selected_data = sorted_data.iloc[:select_num]
		print(selected_data)
		high_value_user = pd.concat([high_value_user, selected_data], ignore_index=True)
		del data, sorted_data, selected_data
	print("High value user:")
	print(high_value_user)
	parquet_output = os.path.join(data_file, f"high_value_user.parquet");
	high_value_user.to_parquet(parquet_output)


def data_high_value_user():
	data_high_value_user_sub("data/10G_data_new", 8)
	data_high_value_user_sub("data/30G_data_new", 16)


def main():
	start_time = time.time()
	data_high_value_user()
	end_time = time.time()
	execution_time = end_time - start_time
	print(f"Execution time: {execution_time:.2f}s")


if __name__ == '__main__':
	main()
