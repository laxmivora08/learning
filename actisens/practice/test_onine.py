#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 16:44:23 2022

@author: stellapps
"""

import sys
# you can write to stdout for debugging purposes, e.g.
# print ""this is a debug message""
def solution():
 
# Following is the part of the program and is provided as an assistance to read the input.
    N=input()
    words=N.split(",")
    words.sort()
    new=",".join(words)
    print(new)

solution()