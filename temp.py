# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
n=int(input("Enter the dimensions of 2d matrix :"))
ms=[]
for i in range(n):
    l=[]
    for j in range(n):
        l.append(0)
    ms.append(l)
    
i=n//2
j=n-1
count=n*n
itr=1
while(itr<=count):
    if(i==-1 and j==n):
        i=0
        j=n-2
    else:
        if(i<0):
            i=n-1
        if(j==n):
            j=0
    if(ms[i][j]!=0):
        i=i+1
        j=j-2
        continue
    else:
        ms[i][j]=itr
        itr+=1
    i-=1
    j+=1
for i in range(n):
        for j in range(n):
            print(ms[i][j],end=' ')
        print()
            

            
