import fool
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


df = pd.read_excel("data/news_2016_2020.xlsx", index_col=0)
df.shape

s = df["content"][1]

print(fool.cut(s))
# ['一个', '傻子', '在', '北京']