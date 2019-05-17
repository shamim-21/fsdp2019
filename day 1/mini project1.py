# -*- coding: utf-8 -*-
"""
Created on Mon May 13 12:34:50 2019

@author: Sammu
"""

import random
secret_no=randint(0,10)
while True:
    if guess_number<7:
        guess_number=input("enter no")
    else:
        break
    
x=secret_no-guess_number 

if guess_number is secret_no:
    print("you win and computer lose")
elif x<5 or x==5:
    print("too high")
elif:
    print("too low")
    
else:
    print("you lose and computer win") 
    print("secret no =",secret_no)
    print("no you select=",number)
