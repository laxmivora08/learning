#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 18:55:42 2021

@author: stellapps
"""
#
num1 = 0
def out_func():
  num1 = 1
  def in_func():
    global num1
    num1 = 2

  in_func()
  return num1

num2 = out_func()
print(num1, num2)

#x = ['ab', 'cd'] 
#for i in x:
#    x.append(i.upper()) 
#print(x)
#print(0.7+0.2==0.9)