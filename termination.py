# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 17:33:49 2016

@author: evgeniy
"""

import os
import time
os.mkdir('Termination')
os.chdir('Termination')

for item in os.listdir():
    os.rename(item, time.strftime('%d.%m.%Y')+item)
    
