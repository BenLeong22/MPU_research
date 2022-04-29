# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import fool

df = pd.read_excel("data/news_2016_2020.xlsx", index_col=0)
all_list =[]
def printresult(list):
    str =""
    list_text=[]
    for a,pos in list:
        print(pos)
        if "w" not in pos:
            list_text.append(a)
    print(list_text)
    return list_text

for text in df["content"]:
    tem_text=fool.pos_cut(str(text))
    tem_text=printresult(tem_text[0])
    all_list.append(tem_text)

df["seg"]=pd.Series(all_list)

df.to_excel("data/seg_news_2016_2020.xlsx")