#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 14:25:25 2021

@author: stellapps
"""

from pathlib import Path
import shutil
#55 22 * * * /usr/bin/python3 /home/stellapps/my_workspace/actisens/archieve_automation.py
src_path = '/home/stellapps/my_workspace/copy'
trg_path = '/home/stellapps/my_workspace/move'

for src_file in Path(src_path).glob('*.*'):
    shutil.move(str(src_file), str(trg_path))