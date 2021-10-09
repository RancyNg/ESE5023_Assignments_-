# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 22:14:14 2021

@author: Rancy Ng
"""

def Pascal_triangle(k):
    i=k
    lst1=[1]
    if i==1:
        print(lst1)
    elif i>1:
        print(lst1)
        num=1
        while num<k:
              lst2=lst1.append(0)
              #I got inspired by reading https://www.cnblogs.com/findlisa/p/10179160.html
              cl=[lst1[i-1]+lst1[i] for i in range(len(lst1))]
              lst1=cl
              print(lst1)
              num=num+1
  
                  