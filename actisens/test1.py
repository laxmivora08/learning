#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 18:55:02 2021

@author: stellapps
"""

#num1 = 0
#def out_func():
#  num1 = 1
#  def in_func():
#    nonlocal num1
#    num1 = 2
#
#  in_func()
#  return num1
#
#num2 = out_func()
#print(num1, num2)
#print(0.7+0.2==0.9)
def my_func(n):
  if n <= 0:
    return False
  return (n & (n-1)) == 0


n = 18

if __name__ == "__main__":
  print(my_func(n))