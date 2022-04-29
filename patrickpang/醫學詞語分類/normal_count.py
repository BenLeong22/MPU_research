import pandas as pd
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
word_list =word_could_dict.keys()
fre=word_could_dict.values()

data = pd.DataFrame({"word":word_list,"fre":fre})
data.to_excel('data/normal_word_fre.xlsx', sheet_name='sheet1', index=False)

wordcloud = WordCloud(width = 1000, height = 500).generate_from_frequencies(word_could_dict)

plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
plt.savefig('books_read.png')

#<------普通統計 End--------->