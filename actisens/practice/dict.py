#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 14:43:46 2022

@author: stellapps
"""

#dict={'1':"laxmi","surname":['vora','bhatt']}
#print(dict[][1])
# Python3 code to iterate through all keys in a dictionary

statesAndCapitals = {
					'Gujarat' : 'Gandhinagar',
					'Maharashtra' : 'Mumbai',
					'Rajasthan' : 'Jaipur',
					'Bihar' : 'Patna'
					}
					
print('List Of given states:\n')
for x in statesAndCapitals: # to print keys
    print(x)
for y in statesAndCapitals.values(): # to print values
    print(y)
# Iterating over keys
for state,capital in statesAndCapitals.items():  #toprintkey values
	print("state is",state,"capital is",capital)
    
