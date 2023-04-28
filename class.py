# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 19:27:19 2022

@author: Hitesh Maan
"""

class sum:
    a=0
    b=0
    def getdata(self):
        self.a=int(input("Enter the value of a :"))
        self.b=int(input("Enter the value of b :"))
    def putdata(self):
       print(self.a+self.b)
        
obj=sum()
obj.getdata()
obj.putdata()
