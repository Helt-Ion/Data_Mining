import os
import numpy as np
import pandas as pd
import json
import time


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


def data_purchase_history_items_sub(data_file, part_num, category_mp):
	for ind, parquet_file in enumerate(get_parquet_files(data_file, part_num)):
		print(f"Reading {parquet_file}...")
		data = pd.read_parquet(parquet_file)
		data_items = data['items'].tolist()
		data_categories = list(map(lambda x : list(map(lambda y : category_mp[y], x.tolist())), data_items))
		print(data_categories[:10])
		del data, data_items


def data_purchase_history_items():
	category_mp, price_mp = product_catalog_read("data/product_catalog.json")
	data_purchase_history_items_sub("data/30G_data_new", 1, category_mp)


def main():
	start_time = time.time()
	data_purchase_history_items()
	end_time = time.time()
	execution_time = end_time - start_time
	print(f"Execution time: {execution_time:.2f}s")


if __name__ == '__main__':
	main()
