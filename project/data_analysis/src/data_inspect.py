import os
import numpy as np
import pandas as pd
import time


def data_read():
	print(f"30G data:")
	parquet_file = os.path.join("data/30G_data_new", "part-00000.parquet")
	data = pd.read_parquet(parquet_file)
	first_row = data.iloc[0]
	print(first_row)
	purchase_history = first_row["purchase_history"]
	print("purchase_history:")
	print(purchase_history)
	login_history = first_row["login_history"]
	print("login_history:")
	print(login_history)


def main():
	start_time = time.time()
	data_read()
	end_time = time.time()
	execution_time = end_time - start_time
	print(f"Execution time: {execution_time:.2f}s")


if __name__ == '__main__':
	main()
