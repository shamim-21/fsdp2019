# -*- coding: utf-8 -*-
"""
Created on Tue May 14 13:50:38 2019

@author: Sammu
"""

list1=["34587 Learning Python, Mark Lutz  4 40.95"]
list2=["98762 Programming Python, Mark Lutz 5 56.80"]
list3=["77226 Head First Python, Paul Barry 3 32.95"]
list4=["88112 Einführung in Python3, Bernd Klein  3 24.99"]
list5=[list1,list2,list3,list4]
tuple1=()
list6=[]
for i in list5:
    for j in i:
        y=j.split()[0]
    x=float(j.split()[-1])
    z=float(j.split()[-2])
    xz=x*z
   
    if (xz)<100:
        value=(xz)+10
        w=(y,value)
        list6.append(w)
    else:
        list6.append(w)
        
    
        
        