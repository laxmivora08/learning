#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 12:14:23 2021

@author: stellapps
"""

a = [3, 2, 4, 1, 0, 5]
def sorted(a):
    len1=len(a)
    print(len1)
    for i in range(len1-1):
        if a[i]>a[i+1]:
            swap(a[i],a[i+1])
            
def swap(a,b):
    temp=a
    b=a
    b=temp
    return a,b
    
if __name__=='__main__':
    sorted(a)
    