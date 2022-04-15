import datetime
import requests
from bs4 import BeautifulSoup
import json

url_list=[]
page_list=[]
content_list=[]
content_data=[]
content_data = []
content_list = []
content_data = []
date = datetime.datetime(2020, 7, 7)
while(date<datetime.datetime.now()):
    print(date)
    year =str(date.year)
    month= '{:02d}'.format(date.month)
    day  ='{:02d}'.format(date.day)

    url ='http://www.macaodaily.com/html/'+year+'-'+month+'/'+day+'/node_2.htm'
    url_list.append(url)
    date= date+datetime.timedelta(days=7)

print(url_list)
print('list here')

for link in url_list:
    r = requests.get(link, auth=('user', 'pass'))

    r.encoding ='utf-8'
    r.text

    soup = BeautifulSoup(r.text, 'html.parser')

    sub_url =link[:-10]
    sub_url_list =[]
    for link in soup.findAll('a', href=True, text=['第D03版：學生報','第D04版：學生報','第D05版：學生報','第D06版：學生報','第E03版：學生報','第E04版：學生報','第E05版：學生報','第E06版：學生報']):
            page_list.append(sub_url+link.attrs['href'])


print(page_list)

for link in page_list:
    r = requests.get(link, auth=('user', 'pass'))
    r.encoding = 'utf-8'
    r.text
    soup = BeautifulSoup(r.text, 'html.parser')
    el = soup.select_one('#Layer1 > table:nth-child(3)')


    for a in soup.find_all('a', href=True):

        if 'content' in str(a):
            content_list.append(link[:-11] + a['href'])


res = []
for i in content_list:
    if i not in res:
        res.append(i)

content_list =res


for link in content_list:
    r = requests.get(link, auth=('user', 'pass'))
    r.encoding = 'utf-8'
    r.text
    soup = BeautifulSoup(r.text, 'html.parser')
    el = soup.select_one('#Layer1 > table:nth-child(3)')



    mydivs = soup.find_all("a", {"class": "thickbox"})
    if mydivs != []:
        img_list = 'http://www.macaodaily.com/' + mydivs[0]['href'][8:]

    else:
        for a in soup.find_all('founder-content'):

            tittle = a.find_all("p")[0]
            tittle = str(tittle)
            tittle = tittle.replace('<p>', "")
            tittle = tittle.replace('</p>', "")
            tittle = tittle.replace('\xa0', '')
            if '點評' in tittle:
                break
            end = a.find_all("p")[-2]
            tem_content = a.find_all("p")[1:-2]

            end = str(end)
            end = end.replace('</p>', "")
            end = end.replace('<p>', "")
            end = end.split()

            if len(end) != 3:
                end = ['', '', '']

            content = ''

            date = link[31:35] + '-' + link[36:38] + '-' + link[39:41]

            for text in tem_content:
                text = str(text)
                text = text.replace('<p></p>', "")
                text = text.replace('<p>', '')
                text = text.replace('\xa0', '')
                text = text.replace('</p>', '')
                content = content + text
            result = {
                "tittle": tittle,
                "content": content,
                "author": end[0],
                "school": end[1],
                "grade": end[2],
                "date": date,
                "link": link
            }
            content_data.append(result)
            print(content_data)



with open('json_data.json', 'w',encoding="utf-8") as outfile:
    json.dump(content_data, outfile, ensure_ascii=False)