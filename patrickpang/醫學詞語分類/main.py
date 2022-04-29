import pandas as pd
from nltk.tokenize import RegexpTokenizer
import re
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

df = pd.read_excel (r'data/search_term.xlsx')
terms= df["Search Term"]
Searches=df["Total Unique Searches"]

all_term =[]

for a in terms:
    spt=a.split();
    for sub_item in spt:
        all_term.append(sub_item)

#<------普通統計--------->
word_could_dict=Counter(all_term)
print(word_could_dict)
# wordcloud = WordCloud(width = 1000, height = 500).generate_from_frequencies(word_could_dict)
#
# plt.figure(figsize=(15,8))
# plt.imshow(wordcloud)
# plt.axis("off")
# plt.show()
# plt.savefig('yourfile.png', bbox_inches='tight')
# plt.close()
#<------普通統計 End--------->

#<------計埋Fre統計--------->
new_fre={}
word_list=[]
fre=[]
for word in word_could_dict:
    num=0
    idx =0
    while idx<len(terms):

        spt = terms[idx].split()
        if word in spt:
            num+=Searches[idx]

        idx=idx+1
    print(str(word) +"--"+ str(num))
    word_list.append(str(word))
    fre.append(num)

data = pd.DataFrame({"word":word_list,"fre":fre})
data.to_excel('word_fre.xlsx', sheet_name='sheet1', index=False)