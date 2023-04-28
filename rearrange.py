# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 09:43:55 2022

@author: Hitesh Maan
"""

import re
def rearrange(name):
    result=re.search(r"^([\w. ]*),[ ]*([\w. ]*)[ ]*$",name)
    if result is None:
        return name
    #return "{} {}".format() 
    return f"{result[2]} {result[1]}"
    