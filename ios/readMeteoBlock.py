from ios.FortranFormat import FortranLine, FortranFormat
import numpy as np
from datetime import datetime

frmt="F7.1,F7.0,F7.1,F7.1,F7.0,F7.2,F7.0,F7.0,F7.1,F7.1,F7.1"
format=FortranFormat(frmt)

def readMeteoFile(fileobj, skiprows=5):
    """
    """
    skipr=skiprows

    P = []
    Z = []
    T = []
    DWPT = []
    RELH = []
    MIXR = []
    DRCT = []
    SKNT = []
    THTA = []
    THTE = []
    THTV = []
    
    try:
        for i in range(skipr):
            fileobj.readline()
            
        for line in fileobj:            
            [p,z,t, dwpt, relh, mixr, drct, sknt, thta, thte, thtv]=FortranLine(line,format)
            if t is None:
                t=np.nan
            
            P.append(p*100.0)
            Z.append(z)
            T.append(t+273.15)
            DWPT.append(dwpt)
            RELH.append(relh)
            MIXR.append(mixr)
            DRCT.append(drct)
            SKNT.append(sknt)
            THTA.append(thta)
            THTE.append(thte)
            THTV.append(thtv)
           
            
    except Exception, e:
        print "Error occured! ",e
    finally:
        fileobj.close()

        
    
    return {'P':np.array(P, dtype='float64'), 'Z':np.array(Z, dtype='float64'), \
        'T':np.array(T, dtype='float64'), 'DWPT':np.array(DWPT, dtype='float64'), \
        'RELH':np.array(RELH, dtype='float64'), 'MIXR':np.array(MIXR, dtype='float64'), \
        'DRCT':np.array(DRCT, dtype='float64'), 'SKNT':np.array(SKNT, dtype='float64'), \
        'THTA':np.array(THTA, dtype='float64'), 'THTE':np.array(THTE, dtype='float64'), \
        'THTV':np.array(THTV, dtype='float64')}
        

def readMeteoCtx(fileobj, skipline=1):
    """
    """
    skip=skipline
    for i in range(skip):
        fileobj.readline()

    ret = {}    
    for line in fileobj:
        left, right = line.split(':')
        left=left.strip()
        left=left.replace(' ','_').replace('[','').replace(']','').lower()
        right=right.strip()
        
        if 'observation' in left:
            ret[left]=datetime.strptime(right,'%y%m%d/%H%M')
        else:
            ret[left]=float(right)
    fileobj.close()
    return ret