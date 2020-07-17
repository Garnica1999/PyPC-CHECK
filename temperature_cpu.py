# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 01:17:33 2020

@author: wcarl
"""

import clr #package pythonnet


class Temperature:
    def __init__(self):
        self.openhardwaremonitor_hwtypes = ['Mainboard','SuperIO','CPU','RAM','GpuNvidia','GpuAti','TBalancer','Heatmaster','HDD']
        self.cputhermometer_hwtypes = ['Mainboard','SuperIO','CPU','GpuNvidia','GpuAti','TBalancer','Heatmaster','HDD']
        self.openhardwaremonitor_sensortypes = ['Voltage','Clock','Temperature','Load','Fan','Flow','Control','Level','Factor','Power','Data','SmallData']
        self.cputhermometer_sensortypes = ['Voltage','Clock','Temperature','Load','Fan','Flow','Control','Level']
        
        
        self.handle = self.initialize_openhardwaremonitor()

        
    def initialize(self):
        print(self.handle)
        self.fetch_stats(self.handle)
    
    def initialize_openhardwaremonitor(self):
        file = 'OpenHardwareMonitorLib'
        clr.AddReference(file)
    
        from OpenHardwareMonitor import Hardware
    
        handle = Hardware.Computer()
        handle.MainboardEnabled = True
        handle.CPUEnabled = True
        handle.RAMEnabled = True
        handle.GPUEnabled = True
        handle.HDDEnabled = True
        handle.Open()
        return handle
    
    def initialize_cputhermometer(self):
        file = 'CPUThermometerLib'
        clr.AddReference(file)
    
        from CPUThermometer import Hardware
        handle = Hardware.Computer()
        handle.CPUEnabled = True
        handle.Open()
        return handle
    
    def fetch_stats(self, handle):
        
        for i in handle.Hardware:
            i.Update()
            for sensor in i.Sensors:
                self.parse_sensor(sensor)
            for j in i.SubHardware:
                j.Update()
                for subsensor in j.Sensors:
                    self.parse_sensor(subsensor)
    
    
    def parse_sensor(self, sensor):
        if sensor.Value is not None:
            if type(sensor).__module__ == 'CPUThermometer.Hardware':
                sensortypes = self.cputhermometer_sensortypes
                hardwaretypes = self.cputhermometer_hwtypes
            elif type(sensor).__module__ == 'OpenHardwareMonitor.Hardware':
                sensortypes = self.openhardwaremonitor_sensortypes
                hardwaretypes = self.openhardwaremonitor_hwtypes
            else:
                return
            if sensor.SensorType == sensortypes.index('Temperature'):
                print(u"%s %s Temperature Sensor #%i %s - %s\u00B0C" % (hardwaretypes[sensor.Hardware.HardwareType], sensor.Hardware.Name, sensor.Index, sensor.Name, sensor.Value))