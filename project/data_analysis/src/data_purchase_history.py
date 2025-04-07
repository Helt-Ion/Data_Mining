import os
import numpy as np
import pandas as pd
import json
import time


def get_parquet_files(data_file, part_num):
	parquet_files = []
	for i in range(0, part_num):
		parquet_file = os.path.join(data_file, f"part-{i:05d}.parquet");
		parquet_files.append(parquet_file)
	return parquet_files


def data_purchase_history_sub(data_file, part_num):
	for ind, parquet_file in enumerate(get_parquet_files(data_file, part_num)):
		print(f"Reading {parquet_file}...")
		data = pd.read_parquet(parquet_file)
		print(data)
		data_json = data['purchase_history'].apply(json.loads)
		print("Purchase history:")
		print(data_json)
		flattened_data = pd.json_normalize(data_json)
		flattened_data['items'] = flattened_data['items'].apply(lambda x : list(map(lambda y : y['id'], x)))
		flattened_data['items_count'] = flattened_data['items'].apply(len)
		print("Flattened data:")
		print(flattened_data)
		converted_data = pd.concat([data.drop('purchase_history', axis=1), flattened_data], axis=1)
		print("Converted data:")
		print(converted_data)
		parquet_output = os.path.join(data_file, f"part-{ind:05d}_purchase_history.parquet");
		converted_data.to_parquet(parquet_output)
		print(f"Converted data saved to {parquet_output}!")
		del data, data_json, flattened_data, converted_data


def data_purchase_history():
	data_purchase_history_sub("data/10G_data_new", 8)
	data_purchase_history_sub("data/30G_data_new", 16)


def main():
	start_time = time.time()
	data_purchase_history()
	end_time = time.time()
	execution_time = end_time - start_time
	print(f"Execution time: {execution_time:.2f}s")


if __name__ == '__main__':
	main()
