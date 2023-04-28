# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 13:40:06 2022

@author: Hitesh Maan
"""
def bubble(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    print(arr)

arr=[0,8,7,6,5,4,3,2,3,4,5,7,8,9,12,10,18]
print(arr)
bubble(arr)

