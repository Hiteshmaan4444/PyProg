# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 06:36:57 2022

@author: Hitesh Maan
"""


           
if __name__ == "__main__":
    def rec(i,j,prev,new,l,n,count):
        if (i<0 or j<0 or i>=n or j>=n or l[i][j]!=prev ):
            return
        l[i][j]=new
        cor=[[0,1],[1,0],[0,-1],[-1,0]]
        for c in cor:
            x,y=c
            rec(i+x,j+y,prev,new,l,n,count)
    
    n = int(input())
    l=[]
    for i in range(n):
        l.append(list(map(int,input().split())))
    print(l)
    print("After: ")
    count=0
    for i in range(n):
        for j in range(n):
            if l[i][j]==0:
                rec(i,j,0,2,l,n,count)
                count+=1
    
    print(l)
    print(count)

