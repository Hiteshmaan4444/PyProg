# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 14:51:31 2022

@author: Hitesh Maan
"""

def fib(n):
    if(n==1):
        return 0
    if(n==2):
        return 1
    return fib(n-1)+fib(n-2)
n=int(input("Enter the number... "))
for i in range(1,n+1):
    print(fib(i))