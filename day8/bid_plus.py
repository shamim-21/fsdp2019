# -*- coding: utf-8 -*-
"""
Created on Thu May 16 14:07:18 2019

@author: Sammu
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
from collections import OrderedDict
url="https://bidplus.gem.gov.in/bidlists"
response=requests.get(url).text
soup = BeautifulSoup(response,"lxml")

print (soup.prettify())

all_tables=soup.find('table',class_='table')
print(all_tables)
A=[]
B=[]
C=[]
D=[]
E=[]
tb=all_tables.find('tbody')

for row in tb.find_all('tr'):
    cells = row.find_all('td')
    
    if len(cells) == 5:
        
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
import pandas as pd
from collections import OrderedDict

col_name = ["POS","Team","Weighted matchs","points","rating"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E]))
df = pd.DataFrame(col_data) 
df.to_csv("former.csv")                


