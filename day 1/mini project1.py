# -*- coding: utf-8 -*-
"""
Created on Mon May 13 12:34:50 2019

@author: Sammu
"""
import random
secret_number=random.randint(0,10)

i=1
while i<7:
    guess_number=input("enter no")
    i=i+1
    if guess_number not in "1234567890":
        print("enter an integer\nLoser")
    else:
        guess_number=int(guess_number)
        x=secret_number-guess_number 
        if secret_number == guess_number:
            print("you win")
            break
        elif x>5 or x<-5:
            print("too high")
        elif x<2 and x>-2:
            print("too close")
        
        else:
            print("you lose and computer win") 
print("secret number = 
      ",secret_number)
print("guess number =  ",guess_number)

