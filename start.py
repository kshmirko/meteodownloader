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
        Time.units = 'days since 2000-01-01 00:00:00'
        Time.calendar = 'standard'

        PRES = f.createVariable('PRES','f4',('time', 'Len',))
        PRES.unit = 'Pa'
        PRES.description = 'Atmospheric pressure'
        
        TEMP = f.createVariable('TEMP','f4',('time', 'Len',))
        TEMP.units = 'Celsius deg'
        TEMP.description = 'Atmospheric temperature'
        
        HGHT = f.createVariable('HGHT','f4',('time', 'Len',))
        HGHT.units = 'meters'
        HGHT.description = 'Altitude above the mean sea level'
        
        RELH = f.createVariable('RELH','f4',('time', 'Len',))
        RELH.units = '%'
        RELH.description = 'Atmospheric relative humidity'
        
        SKNT = f.createVariable('SKNT','f4',('time', 'Len',))
        SKNT.units = 'knots'        
        
        MIXR = f.createVariable('MIXR','f4',('time', 'Len',))
        MIXR.units = 'g/kg'
    
        DRCT = f.createVariable('DRCT','f4',('time', 'Len',))
        DRCT.units = 'deg'
        
        THTA = f.createVariable('THTA','f4',('time', 'Len',))
        THTA.units = 'K'
        
        THTE = f.createVariable('THTE','f4',('time', 'Len',))
        THTE.units = 'K'
        
        THTV = f.createVariable('THTV','f4',('time', 'Len',))
        THTV.units = 'K'        
        f.close()