#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 21:56:10 2021

@author: stellapps
"""
import os
from pathlib import Path
category={'Documents':['.xls','.csv','.pdf'],
'Images':['.png'],
'code':['.py']}
def pick_dic(value):
    for cat,suff in category.items():
        for suffix in suff:
            if suffix==value:
                return cat
print(pick_dic('.pdf'))
def organize():
    for item in os.scandir():
        filepath=Path(item)
        filetype=filepath.suffix.lower()
        directory=pick_dic(filetype)
        directory_path=Path(directory)
        if directory_path.is_dir!=True:
            directory_path.mkdir()
        filepath.rename(directory_path)
