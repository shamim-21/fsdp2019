# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:23:27 2019

@author: Sammu
"""
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup 
import requests
url="https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"
source=requests.get(url).text
soup = BeautifulSoup(source,"lxml")
a=[]
b=[]
labels='Rajasthan','Madhya Pradesh','Maharashtra','Uttar Pradesh','Gujarat','Karnataka'
all_tables=soup.find_all('table')
right_table=soup.find('table',class_='wikitable')
i=0
for row in right_table.findAll('tr'):
    cell=row.findAll('td')
    if len(cell)==7:
        a.append(cell[1].text)
        b.append(cell[4].text)
        i=i+1
    if i==6:
        break

plt.pie(b,labels=a)
plt.axis('equal')  
plt.show()        


