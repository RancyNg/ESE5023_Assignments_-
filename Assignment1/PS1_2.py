# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 16:16:51 2021

@author: Rancy Ng
"""

#2.1
#I got inspired by reading 'blog.csdn.net/weixin_39590868/article/details/113080569'
import numpy as np
M1=(np.random.randint(0,50,(5,10)))
M2=(np.random.randint(0,50,(10,5)))

#2.2
def Matrix_multip(M1,M2):
    #I got inspired by reading https://jingyan.baidu.com/article/22a299b51cf8d69e18376a57.html
    M3= np.zeros((5,5))
    c=[0,1,2,3,4]
    for a in c:
       l1=M1[a,:]
       for i in c:        
          l2=M2[:,i]
          cl=l1*l2
          print(cl)
          num=0
          #I got inspired by reading https://www.runoob.com/python3/python-sum-list.html
          for ele in cl:
             num = num + ele
          M3[a,i]=num    
    
