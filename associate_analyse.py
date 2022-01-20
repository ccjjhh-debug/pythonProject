# -*- coding:UTF-8 -*-
# @time: 2022-01-18 20:56
# @file: associate_analyse.py
# @software: PyCharm
# author CJH

import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
#显示所有列
pd.set_option('display.max_columns',None)
#显示所有行
pd.set_option('display.max_rows',None)

data={'ID':[1,2,3,4,5,6],
     'Onion':[1,0,0,1,1,1],
     'Potato':[1,1,0,1,1,1],
     'Burger':[1,1,0,0,1,1],
     'Milk':[0,1,1,1,0,1],
     'Beer':[0,0,1,0,1,0]
}
df=pd.DataFrame(data)

frequent_itemsets=apriori(df[['Onion','Potato','Burger','Milk','Beer']],min_support=0.50,use_colnames=True)

rules = association_rules(frequent_itemsets,metric='lift',min_threshold=1)

var = rules[(rules['lift'] > 1.125) & (rules['confidence'] > 0.8)]
# 根据实际业务需求进行筛选，选取置信度大于0.8，提升度大于1.125