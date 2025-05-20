import os
import numpy as np
import pandas as pd
import json
import time
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd


def apriori_process_sub(data_file, support_threshold, confidence_threshold):
	parquet_file = os.path.join(data_file, "data_categories.parquet")
	data = pd.read_parquet(parquet_file)
	# 使用Apriori算法找到频繁项集
	frequent_itemsets = apriori(data, min_support=support_threshold, use_colnames=True)
	# 生成关联规则
	rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=confidence_threshold)
	# 显示频繁项集和关联规则
	print("频繁项集:")
	print(frequent_itemsets)
	print("\n关联规则:")
	print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
	del data


def apriori_process():
	print("Real data:")
	apriori_process_sub("data/30G_data_new", 0.02, 0.4)
	print("Random data:")
	apriori_process_sub("data/random_data", 0.02, 0.4)


def main():
	start_time = time.time()
	apriori_process()
	end_time = time.time()
	execution_time = end_time - start_time
	print(f"Execution time: {execution_time:.2f}s")


if __name__ == '__main__':
	main()
