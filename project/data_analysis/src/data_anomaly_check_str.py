import os
import numpy as np
import pandas as pd
import time


def get_parquet_files(data_file, part_num):
	parquet_files = []
	for i in range(0, part_num):
		parquet_file = os.path.join(data_file, f"part-{i:05d}.parquet");
		parquet_files.append(parquet_file)
	return parquet_files


def data_tally(data_frame, by):
	return data_frame[by].value_counts().sort_index()


def output_info(data_file, data_frame, txt_name):
	output_txt = os.path.join(data_file, txt_name)
	with open(output_txt, "w", encoding='utf-8') as f:
		for e in data_frame.index:
			print(e, file=f)
	print(f"Info saved to {output_txt}!")


def data_anomaly_check_str_sub(data_file, part_num):
	for ind, parquet_file in enumerate(get_parquet_files(data_file, part_num)):
		data = pd.read_parquet(parquet_file)
		print(data)
		data_gender = data_tally(data, 'gender')
		print("Sort by gender:")
		print(data_gender)
		data_country = data_tally(data, 'country')
		print("Sort by country:")
		print(data_country)
		data_email = data_tally(data, 'email')
		print("Sort by email:")
		print(data_email)
		output_info(data_file, data_email, f"email_info_{ind}.txt")
		data_phone_number = data_tally(data, 'phone_number')
		print("Sort by phone_number:")
		print(data_phone_number)
		output_info(data_file, data_phone_number, f"phone_number_info_{ind}.txt")
		data_address = data_tally(data, 'address')
		print("Sort by address:")
		print(data_address)
		output_info(data_file, data_address, f"address_info_{ind}.txt")


def data_anomaly_check_str():
	data_anomaly_check_str_sub("data/10G_data_new", 8)
	data_anomaly_check_str_sub("data/30G_data_new", 16)


def main():
	start_time = time.time()
	data_anomaly_check_str()
	end_time = time.time()
	execution_time = end_time - start_time
	print(f"Execution time: {execution_time:.2f}s")


if __name__ == '__main__':
	main()
