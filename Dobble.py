# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 12:11:45 2022

@author: Hitesh Maan
"""

import random
import string
card1=[0]*5
card2=[0]*5
pos1=random.randint(0, 4)
pos2=random.randint(0, 4)
symbols=[]
symbols=list(string.ascii_letters)
samesymbol=random.choice(symbols)
symbols.remove(samesymbol)
if(pos1==pos2):
    card1[pos1]=samesymbol
    card2[pos1]=samesymbol
if(pos1!=pos2):
    card1[pos1]=samesymbol
    card2[pos2]=samesymbol
    card1[pos2]=random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1]=random.choice(symbols)
    symbols.remove(card2[pos1])
i=0
while(i<5):
    if(i!=pos1 and i!=pos2):
        card1[i]=random.choice(symbols)
        symbols.remove(card1[i])
        card2[i]=random.choice(symbols)
        symbols.remove(card2[i])
    i+=1

print(card1)
print(card2)
ch=input("Enter the same letter :" )
if(ch==samesymbol):
    print("You Won!!")
if(ch!=samesymbol):
    print("Better luck next time")
       