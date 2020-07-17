# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 01:00:38 2020

@author: wcarl
"""

import os
import subprocess as sp

def clear(so):
    if so == 'Windows':
        os.system('cls')
    elif so == 'Linux':
        os.system('clear')
    elif so == 'OS X':
        sp.call('cls',shell=True)