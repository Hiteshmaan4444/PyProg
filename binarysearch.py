# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 13:08:54 2022

@author: Hitesh Maan
"""
arr=[]
for i in range(1,10001):
    arr.append(i)
ele=int(input("Enter the number to search"))
beg=0;
end=len(arr)-1
mid=(beg+end)//2
flag=0
count=0
while(beg<end):
    count+=1
    if(arr[mid]==ele):
        print("element is present !!")
        flag=1
        break
    elif(arr[mid]>ele):
        end=mid-1
    elif(arr[mid]<ele):
        beg=mid+1
    mid=(beg+end)//2
if(flag==0):
    print("Element not present")
print(count)