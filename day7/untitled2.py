# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:05:28 2019

@author: Sammu
"""
import requests

url1 = "http://api.openweathermap.org/data/2.5/weather" 
url2 = "?q=Jaipur"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3
print (url)


shamim = requests.get(url)

xyz = shamim.json()


