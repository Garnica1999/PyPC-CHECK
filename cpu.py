# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 13:18:04 2020

@author: wcarl
"""

import psutil
from cpuinfo import get_cpu_info

from temperature_cpu import Temperature

class Cpu:
    
    def __init__(self):
        self.temperature = Temperature()
        
        self.__cpu_dict = get_cpu_info()
        self.__complete_cpu_information()
        self.get_usage_per_core()
        #self.__update_temperatures()
    
    def get_name_cpu(self):
        return self.__cpu_dict['brand_raw']
    
    def get_cores_cpu(self):
        return self.__cpu_dict['cores']
    
    def get_logical_cores_cpu(self):
        return self.__cpu_dict['logical_cores']
    
    def get_architecture_bits(self):
        return self.__cpu_dict['bits']
    
    def get_vendor(self):
        return self.__cpu_dict['vendor_id_raw']
    
    def get_frecuency_cpu(self):
        return self.__cpu_dict['hz_actual']
    
    def get_set_instructions(self):
        return self.__cpu_dict['flags']
    
    def get_current_frecuency_cpu(self):
        return self.__cpu_dict['current_frecuency']
        
    def get_max_frecuency_cpu(self):
        return self.__cpu_dict['cpufreq_max']

    def get_min_frecuency_cpu(self):
        return self.__cpu_dict['cpufreq_min']
        
    def get_usage_per_core(self):
        for i in range(self.__cpu_dict['cores']):
            key = 'core_usage_' + str(i)
            self.__cpu_dict[key] = None
        
        for i, porcentage in enumerate(psutil.cpu_percent(interval = 1, percpu= True)):
            key = 'core_usage_' + str(i)
            self.__cpu_dict[key] = porcentage
            
    def __complete_cpu_information(self):
        cpufreq = psutil.cpu_freq()
        self.__cpu_dict['current_frecuency'] = f'{cpufreq.current:.2f}'
        self.__cpu_dict['cores'] = psutil.cpu_count(logical=False)
        self.__cpu_dict['logical_cores'] = psutil.cpu_count(logical=True)
        
        self.__cpu_dict['cpufreq_max'] = cpufreq.max
        self.__cpu_dict['cpufreq_min'] = cpufreq.min
        
        
    def get_cpu_info(self):
        self.get_usage_per_core()
        return self.__cpu_dict
    
    def __update_temperatures(self):
        self.temperature.initialize()
        #CPUHandle = tc.initialize_cputhermometer()
        #tc.fetch_stats(CPUHandle)