# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 21:46:19 2020

@author: wcarl
"""

import psutil

class RamBuilder:
    def __init__(self):
        self.__svmem = psutil.virtual_memory()
        self.__ram_builder = {}
        
    def get_bytes(self, bytes, suffix = 'B'):
        factor = 1024
        for unit in ['', 'K', 'M', 'G', 'T', 'P']:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor
            
    def build(self):
        total_mem = self.get_bytes(self.__svmem.total)
        available_mem = self.get_bytes(self.__svmem.available)
        used_mem = self.get_bytes(self.__svmem.used)
        percentage_mem = self.get_bytes(self.__svmem.percent)
        
        self.__ram_builder['total_memory'] = total_mem
        self.__ram_builder['available_memory'] = available_mem
        self.__ram_builder['used_memory'] = used_mem
        self.__ram_builder['percentage_memory'] = percentage_mem
        
        return self.__ram_builder
            
    