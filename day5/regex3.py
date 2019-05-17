# -*- coding: utf-8 -*-
"""
Created on Sat May 11 17:46:51 2019

@author: Sammu
"""

import re
while True:
   credit_no=input("enter credit card no")
   if not credit_no:
       break
   #result=re.match(r'^[456]+[0-9]{3}\-?[0-9]{4}\-?[0-9]{4}\-?[0-9]{4}\-?$',credit_no)
   result=re.match(r'^[456](\d{15}|\d{3}-(\d{4}-){2}\d{4})$',credit_no)
   consec = re.search(r"(\d)\1{3,}",credit_no.replace("-",""))
   if result and not consec:
       print(credit_no)
   else :

       print("invalid credit no")