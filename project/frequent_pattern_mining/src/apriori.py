import os
import numpy as np
import pandas as pd
import json
import time
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd


def apriori_process():
	# n = 13500000
	n = 1350000
	parquet_file = os.path.join("data/30G_data_new", "data_categories.parquet")
	data = pd.read_parquet(parquet_file)
	# print(data)
	data_part = data.head(n)
	print(data_part)
	# 使用Apriori算法找到频繁项集
	frequent_itemsets = apriori(data_part, min_support=0.005, use_colnames=True)
	# 生成关联规则
	rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.05)
	# 显示频繁项集和关联规则
	print("频繁项集:")
	print(frequent_itemsets)
	print("\n关联规则:")
	print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])


def main():
	start_time = time.time()
	apriori_process()
	end_time = time.time()
	execution_time = end_time - start_time
	print(f"Execution time: {execution_time:.2f}s")


if __name__ == '__main__':
	main()
