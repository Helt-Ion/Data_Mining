import os
import numpy as np
import pandas as pd
import json
import time
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd


def product_catalog_read(json_file):
	print(f"Reading {json_file}...")
	category_mp, price_mp = {}, {}
	with open(json_file, 'r', encoding='utf-8') as file:
		product_catalog = json.load(file)['products']
		for v in product_catalog:
			product_id = v['id']
			category_mp[product_id] = v['category']
			price_mp[product_id] = v['price']
	return category_mp, price_mp


def get_parquet_files(data_file, part_num):
	parquet_files = []
	for i in range(0, part_num):
		parquet_file = os.path.join(data_file, f"part-{i:05d}_purchase_history.parquet")
		parquet_files.append(parquet_file)
	return parquet_files


def data_process_sub(data_file, part_num, category_mp):
	data_categories = []
	for ind, parquet_file in enumerate(get_parquet_files(data_file, part_num)):
		print(f"Reading {parquet_file}...")
		data = pd.read_parquet(parquet_file)
		data_items = data['items'].tolist()
		for item in data_items:
			data_categories.append(list(map(lambda x : category_mp[x], item.tolist())))
		del data, data_items
	print(data_categories[:5])
	te = TransactionEncoder()
	te_ary = te.fit(data_categories).transform(data_categories)
	converted_data = pd.DataFrame(te_ary, columns=te.columns_)
	print(converted_data)
	parquet_output = os.path.join(data_file, f"data_categories.parquet");
	converted_data.to_parquet(parquet_output)


def data_process():
	category_mp, price_mp = product_catalog_read("data/product_catalog.json")
	data_process_sub("data/30G_data_new", 16, category_mp)


def main():
	start_time = time.time()
	data_process()
	end_time = time.time()
	execution_time = end_time - start_time
	print(f"Execution time: {execution_time:.2f}s")


if __name__ == '__main__':
	main()
