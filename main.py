# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 13:21:33 2020

@author: wcarl
"""

from pc import Pc
from tabulate import tabulate
from utils import clear

import os
import time

pc = Pc()

while(True):
    
    print('='*30, 'CPU INFO', '='*30)
    cpu = pc.get_cpu()
    cpu.temperature.initialize()
    #clear(pc.get_so())
    #print('CPU: {}'.format(cpu.get_name_cpu()))
    #print('CPU Cores: {}'.format(cpu.get_cores_cpu()))
    #print('CPU Threads: {}'.format(cpu.get_logical_cores_cpu()))
    #print('CPU_Max_Frecuency: {}'.format(cpu.get_max_frecuency_cpu()))
    #print('Frecuencia actual: {}'.format(cpu.get_current_frecuency_cpu()))
    
    time.sleep(1)
    