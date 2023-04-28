# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 09:29:39 2022

@author: Hitesh Maan
"""

def fact(n):
    if(n==1):
        return 1
    return n*fact(n-1)

print(fact(4))