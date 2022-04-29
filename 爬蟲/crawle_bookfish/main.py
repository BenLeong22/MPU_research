# -*- coding: utf-8 -*-

from csv import reader
from PIL import Image
import requests

id=[]
large=[]
small=[]
with open('2019-05-19 BookFish data.csv', 'r', encoding = "ISO-8859-1") as read_obj:

    csv_reader = reader(read_obj)

    list_of_rows = list(csv_reader)

row=2
while row <len(list_of_rows) :
    data =list_of_rows[row]

    id.append(data[0])
    large.append(data[5])
    small.append(data[6])
    row =row+1
idx =0
dead =0
deadlist=[]
while idx <len(id):
    name =id[idx]
    print(name)
    if large[idx] !="":
        print(large[idx])
        r_large = requests.get(large[idx])
        if r_large.status_code !=404:
            print(0)
        else:
            dead =dead+1
            deadlist.append(large[idx])
            print(dead)


    if small[idx] !="":
        r_small = requests.get(small[idx])
        if r_small.status_code != 404:
            print(0)
        else:
            dead = dead + 1
            deadlist.append(small[idx])
            print(dead)
    idx =idx+1
    print(deadlist)

print(deadlist)
print(dead)
