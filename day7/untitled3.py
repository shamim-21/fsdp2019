# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:28:48 2019

@author: Sammu
"""
import requests
url1="http://free.currencyconverterapi.com/api/v5/convert"
url2="?q=USD_INR"
url3="&compact=ultra&apiKey=66be94485698694cddeb"
url=url1+url2+url3
shamim=requests.get(url)
xyz=shamim.json()
    

DOLLAR=int(input("enter no"))
print(DOLLAR*xyz["USD_INR"])
