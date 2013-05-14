meteodownloader
===============

This program used to download and store meteorological data in netCDF format.

Aims of the program:
-  Downloads the set of upper-air sounding data and stores it in netcdf3 format


Output file structure presented below

    dimensions:
	time = UNLIMITED ; // (58 currently)
	Len = 300 ;
    variables:
	float Time(time) ;
		Time:units = "days since 1984-02-08 00:00:00" ;
		Time:calendar = "standard" ;
	float PRES(time, Len) ;
		PRES:_FillValue = NaNf ;
		PRES:unit = "[Pa]" ;
		PRES:description = "Atmospheric Pressure" ;
	float TEMP(time, Len) ;
		TEMP:_FillValue = NaNf ;
		TEMP:units = "[celsius]" ;
		TEMP:description = "Temperature" ;
	float HGHT(time, Len) ;
		HGHT:_FillValue = NaNf ;
		HGHT:units = "[meter]" ;
		HGHT:description = "Geopotential Height" ;
	float DWPT(time, Len) ;
		DWPT:_FillValue = NaNf ;
		DWPT:units = "[celsius]" ;
		DWPT:description = "Dewpoint Temperature" ;
	float RELH(time, Len) ;
		RELH:_FillValue = NaNf ;
		RELH:units = "[%]" ;
		RELH:description = "Relative Humidity" ;
	float SKNT(time, Len) ;
		SKNT:_FillValue = NaNf ;
		SKNT:units = "[knot]" ;
		SKNT:description = "Wind Speed" ;
	float MIXR(time, Len) ;
		MIXR:_FillValue = NaNf ;
		MIXR:units = "[gram/kilogram]" ;
		MIXR:description = "Mixing Ratio" ;
	float DRCT(time, Len) ;
		DRCT:_FillValue = NaNf ;
		DRCT:units = "[degrees true]" ;
		DRCT:description = "Wind Direction" ;
	float THTA(time, Len) ;
		THTA:_FillValue = NaNf ;
		THTA:units = "[kelvin]" ;
		THTA:description = "Potential Temperature" ;
	float THTE(time, Len) ;
		THTE:_FillValue = NaNf ;
		THTE:units = "[kelvin]" ;
		THTE:description = "Equivalent Potential Temperature" ;
	float THTV(time, Len) ;
		THTV:_FillValue = NaNf ;
		THTV:units = "[kelvin]" ;
		THTV:description = "Virtual Potential Temperature" ;
	int STID(time) ;
		STID:units = "[N/A]" ;
		STID:description = "Station WM id" ;
	float SOBS(time) ;
		SOBS:units = "days since 1984-02-08 00:00:00" ;
		SOBS:calendar = "standard" ;
	float SLAT(time) ;
		SLAT:_FillValue = NaNf ;
		SLAT:units = "[degrees true]" ;
		SLAT:description = "Station latitude" ;
	float SLON(time) ;
		SLON:_FillValue = NaNf ;
		SLON:units = "[degrees true]" ;
		SLON:description = "Station longitude" ;
	float SELV(time) ;
		SELV:_FillValue = NaNf ;
		SELV:units = "[meter]" ;
		SELV:description = "Station elevation" ;
	float SHOW(time) ;
		SHOW:_FillValue = NaNf ;
		SHOW:units = "[celsius]" ;
		SHOW:description = "Showalter index" ;
	float LIFT(time) ;
		LIFT:_FillValue = NaNf ;
		LIFT:units = "[celsius]" ;
		LIFT:description = "Lifted index" ;
	float LFTV(time) ;
		LFTV:_FillValue = NaNf ;
		LFTV:units = "[celsius]" ;
		LFTV:description = "LIFT computed by using virtual temperature" ;
	float SWET(time) ;
		SWET:_FillValue = NaNf ;
		SWET:units = "[N/A]" ;
		SWET:description = "SWEAT index" ;
	float KINX(time) ;
		KINX:_FillValue = NaNf ;
		KINX:units = "[N/A]" ;
		KINX:description = "K index" ;
	float CTOT(time) ;
		CTOT:_FillValue = NaNf ;
		CTOT:units = "[N/A]" ;
		CTOT:description = "Cross Totals index" ;
	float VTOT(time) ;
		VTOT:_FillValue = NaNf ;
		VTOT:units = "[N/A]" ;
		VTOT:description = "Vertical Totals index" ;
	float TTOT(time) ;
		TTOT:_FillValue = NaNf ;
		TTOT:units = "[N/A]" ;
		TTOT:description = "Totals Totals index" ;
	float CAPE(time) ;
		CAPE:_FillValue = NaNf ;
		CAPE:units = "[J/kg]" ;
		CAPE:description = "Convective Available Potential Energy" ;
	float CAPV(time) ;
		CAPV:_FillValue = NaNf ;
		CAPV:units = "[J/kg]" ;
		CAPV:description = "CAPE computed by using the virtual temperature." ;
	float CINS(time) ;
		CINS:_FillValue = NaNf ;
		CINS:units = "[J/kg]" ;
		CINS:description = "Convective inhibition" ;
	float CINV(time) ;
		CINV:_FillValue = NaNf ;
		CINV:units = "[J/kg]" ;
		CINV:description = "CINS computed by using the virtual temperature." ;
	float BRCH(time) ;
		BRCH:_FillValue = NaNf ;
		BRCH:units = "[N/A]" ;
		BRCH:description = "Bulk Richardson number" ;
	float BRCV(time) ;
		BRCV:_FillValue = NaNf ;
		BRCV:units = "[N/A]" ;
		BRCV:description = "BRCH computed by using CAPV" ;
	float LCLT(time) ;
		LCLT:_FillValue = NaNf ;
		LCLT:units = "[kelvin]" ;
		LCLT:description = "Temperature at the LCL, the lifting condensation level, from an average of the lowest 500 meters" ;
	float LCLP(time) ;
		LCLP:_FillValue = NaNf ;
		LCLP:units = "[hPa]" ;
		LCLP:description = "Pressure at the LCL, the lifting condensation level, from an average of the lowest 500 meters" ;
	float MLTH(time) ;
		MLTH:_FillValue = NaNf ;
		MLTH:units = "[kelvin]" ;
		MLTH:description = "Mean mixed layer THTA" ;
	float MLMR(time) ;
		MLMR:_FillValue = NaNf ;
		MLMR:units = "[g/kg]" ;
		MLMR:description = "Mean mixed layer MIXR" ;
	float THTK(time) ;
		THTK:_FillValue = NaNf ;
		THTK:units = "[meter]" ;
		THTK:description = "1000 mb to 500 mb thickness" ;
	float PWAT(time) ;
		PWAT:_FillValue = NaNf ;
		PWAT:units = "[mm]" ;
		PWAT:description = "Precipitable water for the entire sounding" ;
