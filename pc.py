# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 21:23:01 2020

@author: wcarl
"""

import psutil
import sys

from cpu import Cpu
from ram import Ram


class Pc:
    def __init__(self):
        self.__cpu = Cpu()
        self.__ram = Ram()
    
    def get_cpu_dict(self):
        return self.__cpu_dict
    
    def get_cpu(self):
        return self.__cpu
    
    def get_ram(self):
        return self.__ram
    
    def get_so(self):
        platforms = {
            'linux1' : 'Linux',
            'linux2' : 'Linux',
            'darwin' : 'OS X',
            'win32' : 'Windows'
        }
        if sys.platform not in platforms:
            return sys.platform
        
        return platforms[sys.platform]