# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 23:13:43 2021

@author: Rancy Ng
"""

def Print_values(a,b,c):
    if(a>b):
        if(b>c):
            print(a,b,c)
        elif(b<c):
            if(a>c):
                print(a,c,b)
            elif(a<c):
                print(c,a,b)
    else:
        if(b>c):
            print("The answer was not given")
        elif(b<c):
            print(c,b,a)