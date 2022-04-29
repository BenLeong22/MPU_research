import pandas as pd
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

df = pd.read_excel (r'data/search_term.xlsx')
terms= df["Search Term"]
Searches=df["Total Unique Searches"]

all_term =[]

for a in terms:
    spt=a.split();
    for sub_item in spt:
        all_term.append(sub_item)

word_could_dict=Counter(all_term)
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
data.to_excel('data/fre_word_fre.xlsx', sheet_name='sheet1', index=False)

dict_from_list = dict(zip(word_list, fre))

wordcloud = WordCloud(width = 1000, height = 500).generate_from_frequencies(dict_from_list)

plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
plt.savefig('fre_count_word_clound.png', bbox_inches='tight')
plt.close()