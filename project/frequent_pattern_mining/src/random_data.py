import os
import numpy as np
import pandas as pd
import json
import time
import random
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd


global_category_list = ["电子产品", "服装", "食品", "家居", "办公", "运动户外", "玩具", "母婴", "汽车用品"]


def random_data():
	data_file = "data/random_data"
	data_categories = []
	n = 135000000
	m = 5
	for i in range(n):
		data_categories.append(random.choices(global_category_list, k=random.randint(1, m)))
	print("Categories:")
	print(data_categories[:5])
	te = TransactionEncoder()
	te_ary = te.fit(data_categories).transform(data_categories)
	converted_data = pd.DataFrame(te_ary, columns=te.columns_)
	print("Converted data:")
	print(converted_data)
	parquet_output = os.path.join(data_file, f"data_categories.parquet");
	converted_data.to_parquet(parquet_output)


def main():
	start_time = time.time()
	random_data()
	end_time = time.time()
	execution_time = end_time - start_time
	print(f"Execution time: {execution_time:.2f}s")


if __name__ == '__main__':
	main()
