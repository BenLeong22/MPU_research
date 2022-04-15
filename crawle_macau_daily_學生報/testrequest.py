import requests
from bs4 import BeautifulSoup
import html2text
import json




link='http://www.macaodaily.com/html/2020-08/04/content_1451675.htm'
r = requests.get(link, auth=('user', 'pass'))
r.encoding = 'utf-8'
r.text
soup = BeautifulSoup(r.text, 'html.parser')
el = soup.select_one('#Layer1 > table:nth-child(3)')

content_list = []
content_data =[]

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

        if len(end) !=3:
            end=['','','']

        content = ''


        date=link[31:35]+'-'+link[36:38]+'-'+link[39:41]

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
            "date":date,
            "link":link
        }
        content_data.append(result)
        print(content_data)

