# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 21:54:21 2020

@author: wcarl
"""

from ram_constructor import RamBuilder

class Ram:
    
    def __init__(self):
        ram_builder = RamBuilder()
        self.__ram_dict = ram_builder.build()
        
    def get_total_memory(self):
        return self.__ram_dict['total_memory']
    
    def get_free_memory(self):
        return self.__ram_dict['available_memory']
    
    def get_used_memory(self):
        return self.__ram_dict['used_memory']
    
    def get_percent_used_memory(self):
        return self.__ram_dict['percentage_memory']