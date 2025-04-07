import os
import numpy as np
import pandas as pd
import time


def data_read():
	print(f"10G data:")
	parquet_file = os.path.join("data/10G_data_new", "part-00000.parquet");
	data = pd.read_parquet(parquet_file)
	print(data)
	print(f"30G data:")
	parquet_file = os.path.join("data/30G_data_new", "part-00000.parquet");
	data = pd.read_parquet(parquet_file)
	print(data)
	print("Columns:")
	print(data.columns)
	first_row = data.iloc[0]
	print(first_row)


def main():
	start_time = time.time()
	data_read()
	end_time = time.time()
	execution_time = end_time - start_time
	print(f"Execution time: {execution_time:.2f}s")


if __name__ == '__main__':
	main()
