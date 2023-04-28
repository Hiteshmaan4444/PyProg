# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 09:40:28 2022

@author: Hitesh Maan
"""
import re
line = 'this the line with two numbers 10 and 20'

list = [1,2,3,4,5,6]

def func1(line):
    result=re.search(r'[a-zA-Z ]*([0-9]*)[a-zA-z ]*([\d]*)',line)
    sum = int(result.group(1)) + int(result.group(2))
    return sum

def func(list):
    sum=0
    for i in list:
        sum+=i
    return sum

print(func1(line))