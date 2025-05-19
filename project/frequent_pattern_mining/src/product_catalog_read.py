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
	print(category_mp)


def main():
	start_time = time.time()
	product_catalog_read("data/product_catalog.json")
	end_time = time.time()
	execution_time = end_time - start_time
	print(f"Execution time: {execution_time:.2f}s")


if __name__ == '__main__':
	main()
