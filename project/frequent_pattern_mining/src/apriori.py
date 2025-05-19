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


def apriori_process_sub(data_file, part_num, category_mp):
	for ind, parquet_file in enumerate(get_parquet_files(data_file, part_num)):
		print(f"Reading {parquet_file}...")
		data = pd.read_parquet(parquet_file)
		data_items = data['items'].tolist()
		data_categories = list(map(lambda x : list(map(lambda y : category_mp[y], x.tolist())), data_items))
		te = TransactionEncoder()
		te_ary = te.fit(data_categories).transform(data_categories)
		df = pd.DataFrame(te_ary, columns=te.columns_)
		print(df)
		# 使用Apriori算法找到频繁项集
		frequent_itemsets = apriori(df, min_support=0.02, use_colnames=True)
		# 生成关联规则
		rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.3)
		# 显示频繁项集和关联规则
		print("频繁项集:")
		print(frequent_itemsets)
		print("\n关联规则:")
		print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
		del data, data_items, data_categories, df


def apriori_process():
	category_mp, price_mp = product_catalog_read("data/product_catalog.json")
	apriori_process_sub("data/30G_data_new", 1, category_mp)


def main():
	start_time = time.time()
	apriori_process()
	end_time = time.time()
	execution_time = end_time - start_time
	print(f"Execution time: {execution_time:.2f}s")


if __name__ == '__main__':
	main()
