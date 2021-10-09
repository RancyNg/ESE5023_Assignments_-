# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 15:27:03 2021

@author: Rancy Ng
"""
import numpy as np
num=int(input("enter an number:"))
if num==1:
    print(0)
else:
    #i got inspired by reading http://www.3qphp.com/python/pybase/2887.html
    M=[0 for i in range(num+1)]
    M[1]=0
    M[2]=1
    k=3
    while k<(num+1):
       if k%2!=0:
           M[k]=M[k-1]+1
       else:
           if M[k-1] > M[int(k/2)]:
               M[k] = M[int(k/2)]+1
           else:
               M[k] = M[k-1]+1
       k=k+1
            
    print(M[k-1]);
       




