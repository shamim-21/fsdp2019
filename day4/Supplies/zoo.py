# -*- coding: utf-8 -*-
"""
Created on Fri May 10 17:22:33 2019

@author: Sammu
"""
import csv

with open("zoo.csv","r") as file:
    file1=csv.reader(file,delimiter=",")
    next(file1)
    for row in file1:
        print(row)

animal_data = {}
with open("zoo.csv","r") as file:
    file1=csv.reader(file,delimiter=",")
    next(file1)
    for row in file1:
        if row[0] not in animal_data:
            animal_data[row[0]] = [[int(row[1])],[int(row[2])]]
        else:
            animal_data[row[0]][0].append(int(row[1]))
            animal_data[row[0]][1].append(int(row[2]))

print(animal_data)
dict1={}
def water_req():
    
    for key in animal_data:
        x=sum(animal_data[key][1])
        
        dict1[key]=x
    return dict1
print(water_req()) 
 
def total_water():
    total=0
    for key in dict1:
       total=total+(dict1[key])
    print(total)
total_water()  
      

        
     
    