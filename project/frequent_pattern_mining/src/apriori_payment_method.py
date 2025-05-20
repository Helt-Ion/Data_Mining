import os
import numpy as np
import pandas as pd
import json
import time
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd


def set_to_str(input_set):
	items_str = ", ".join(input_set)
	return f"({items_str})"


def apriori_process_sub(data_file, support_threshold, confidence_threshold):
	parquet_file = os.path.join(data_file, "data_payment_method.parquet")
	data = pd.read_parquet(parquet_file)
	# 使用Apriori算法找到频繁项集
	frequent_itemsets = apriori(data, min_support=support_threshold, use_colnames=True)
	# 生成关联规则
	rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=confidence_threshold)
	# 显示频繁项集和关联规则
	print("Frequent itemsets:")
	for itemsets, support in frequent_itemsets[['itemsets', 'support']].values:
		print(f"{set_to_str(itemsets)}, support: {support:.4f}")
	# 将频繁项集与关联规则储存至txt文件中
	rules_txt_file = os.path.join(data_file, "rules_categories.txt")
	print("\nAssociation rules:")
	with open(rules_txt_file, "w", encoding='utf-8') as f:
		print("Frequent itemsets:", file=f)
		for itemsets, support in frequent_itemsets[['itemsets', 'support']].values:
			print(f"{set_to_str(itemsets)}, support: {support:.4f}", file=f)
		print("\nAssociation rules:", file=f)
		for antecedents, consequents, confidence, support in rules[['antecedents', 'consequents', 'confidence', 'support']].values:
			print(f"{set_to_str(antecedents)} -> {set_to_str(consequents)}, confidence: {confidence:.4f}, support: {support:.4f}")
			print(f"{set_to_str(antecedents)} -> {set_to_str(consequents)}, confidence: {confidence:.4f}, support: {support:.4f}", file=f)
	del data, frequent_itemsets, rules


def apriori_process():
	print("Real data:")
	apriori_process_sub("data/30G_data_new", 0.02, 0.4)


def main():
	start_time = time.time()
	apriori_process()
	end_time = time.time()
	execution_time = end_time - start_time
	print(f"Execution time: {execution_time:.2f}s")


if __name__ == '__main__':
	main()
