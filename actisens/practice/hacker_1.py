#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 11:59:32 2022

@author: stellapps
"""

import sys
import xml.etree.ElementTree as etree
#*<feed xml:lang='en'>
#    <title>HackerRank</title>
#    <subtitle lang='en'>Programming challenges</subtitle>
#    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
#    <updated>2013-12-25T12:00:00</updated>
#</feed>*
def get_attr_number(node):
    # your code goes here
    # XML 1 - Find the Score in Python - Hacker Rank Solution START
    count = 0
    for tag in node:
        count = count + get_attr_number(tag)
    return count + len(node.attrib)
    # XML 1 - Find the Score in Python - Hacker Rank Solution END

if __name__ == '__main__':
    sys.stdin.readline()
    xml =" <feed xml:lang='en'><title>HackerRank</title> <subtitle lang='en'>Programming challenges</subtitle><link rel='alternate' type='text/html' href='http://hackerrank.com/'/><updated>2013-12-25T12:00:00</updated></feed>"
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()

    print(get_attr_number(root))