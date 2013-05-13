# -*- coding: utf-8 -*-
"""
Created on Mon May 13 15:08:24 2013

@author: kshmirko
"""

from netCDF4 import Dataset



class meteoFile(object):    
    def __init__(self, fname):
        self.__fname = fname
        self.datas = []
    
    def add(self, data):
        self.datas.append(data)
        
    def close(self):
        f = Dataset(self.__fname,'w', format='NETCDF3_64BIT')
        time = f.createDimension('time', None)
        Len = f.createDimension('Len',300)
        
        Time = f.createVariable('Time','f4',('time',))
        PRES = f.createVariable('PRES','f4',('time', 'Len',))
        TEMP = f.createVariable('TEMP','f4',('time', 'Len',))
        HGHT = f.createVariable('HGHT','f4',('time', 'Len',))
        RELH = f.createVariable('RELH','f4',('time', 'Len',))
        SKNT = f.createVariable('SKNT','f4',('time', 'Len',))
        MIXR = f.createVariable('MIXR','f4',('time', 'Len',))
        DRCT = f.createVariable('DRCT','f4',('time', 'Len',))
        THTA = f.createVariable('THTA','f4',('time', 'Len',))
        THTE = f.createVariable('THTE','f4',('time', 'Len',))
        THTV = f.createVariable('THTV','f4',('time', 'Len',))
        
        f.close()