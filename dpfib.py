# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 02:54:59 2022

@author: Hitesh Maan
"""
def fuc(n,dp):
     if n==0 or n==1:
             dp[n]=1
             return dp[n]
     if dp[n]:
             return dp[n]
     dp[n]=fuc(n-1,dp)+fuc(n-2,dp)
     return dp[n]

def fib(n):
    dp=[]
    for i in range(n+1):
        dp.insert(n,0)
    print(fuc(i,dp))
    
fib(4)
