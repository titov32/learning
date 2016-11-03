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
    
class Terminal():
    def __init__(self, client, id, serial):
        self.client=client
        self.id=id
        self.serial=serial
    def send(self):
        print('Now sending info)
    def get_file(self,file):
        print ('file get')
    def