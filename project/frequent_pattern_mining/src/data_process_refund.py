import os
import numpy as np
import pandas as pd
import json
import time
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd


global_categories = {
	"电子产品": ["智能手机", "笔记本电脑", "平板电脑", "智能手表", "耳机", "音响", "相机", "摄像机", "游戏机"],
	"服装": ["上衣", "裤子", "裙子", "内衣", "鞋子", "帽子", "手套", "围巾", "外套"],
	"食品": ["零食", "饮料", "调味品", "米面", "水产", "肉类", "蛋奶", "水果", "蔬菜"],
	"家居": ["家具", "床上用品", "厨具", "卫浴用品"],
	"办公": ["文具", "办公用品"],
	"运动户外": ["健身器材", "户外装备"],
	"玩具": ["玩具", "模型", "益智玩具"],
	"母婴": ["婴儿用品", "儿童课外读物"],
	"汽车用品": ["车载电子", "汽车装饰"]
}


def product_catalog_read(json_file):
	print(f"Reading {json_file}...")
	main_category_mp = {}
	for k, v in global_categories.items():
		for e in v:
			main_category_mp[e] = k
	category_mp, price_mp = {}, {}
	with open(json_file, 'r', encoding='utf-8') as file:
		product_catalog = json.load(file)['products']
		for v in product_catalog:
			product_id = v['id']
			category_mp[product_id] = main_category_mp[v['category']]
			price_mp[product_id] = v['price']
	return category_mp, price_mp


def get_parquet_files(data_file, part_num):
	parquet_files = []
	for i in range(0, part_num):
		parquet_file = os.path.join(data_file, f"part-{i:05d}_purchase_history.parquet")
		parquet_files.append(parquet_file)
	return parquet_files


def data_process_refund_sub(data_file, part_num, category_mp):
	data_categories = []
	for ind, parquet_file in enumerate(get_parquet_files(data_file, part_num)):
		print(f"Reading {parquet_file}...")
		data = pd.read_parquet(parquet_file)
		for item, payment_status in data[['items', 'payment_status']].values:
			data_categories.append(list(map(lambda x : category_mp[x], item.tolist())) + [payment_status])
		del data
	print("Categories:")
	print(data_categories[:5])
	te = TransactionEncoder()
	te_ary = te.fit(data_categories).transform(data_categories)
	converted_data = pd.DataFrame(te_ary, columns=te.columns_)
	print("Converted data:")
	print(converted_data)
	parquet_output = os.path.join(data_file, f"data_refund.parquet");
	converted_data.to_parquet(parquet_output)


def data_process_refund():
	category_mp, price_mp = product_catalog_read("data/product_catalog.json")
	data_process_refund_sub("data/30G_data_new", 16, category_mp)


def main():
	start_time = time.time()
	data_process_refund()
	end_time = time.time()
	execution_time = end_time - start_time
	print(f"Execution time: {execution_time:.2f}s")


if __name__ == '__main__':
	main()
