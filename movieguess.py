# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 11:41:12 2022

@author: Hitesh Maan
"""

import random
movies=["inception","Parasite","spiderman","batman"]
score=3;
sample=random.choice(movies);
guess=[]
for i in range(len(sample)):
    guess.append('-')
for i in guess:
    print(i,end='')
found=0
while(found<len(sample)):
    letter=input("Guess the letter in the movie to quit press(#) : ");
    if(letter=='#'):
        break
    flag=0;
    pos=0;
    for i in sample:
        if letter==i:
            guess[pos]=letter
            flag=1
            found+=1
        pos+=1
    for i in guess:
        print(i,end='')
            
    if(flag):
        print("great guess!!")
    else:
        print("No Wrong Guess")
        score-=1;
        print("Lives Remaining :"+ str(score))
        if(score==0):
            print("You Lost !!")
            break
        
if(found==len(sample)-1):
    print("great you did it !!")
print("the movie was: " + sample)