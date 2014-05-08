import numpy as np
def main(fn='STR_STR.OUT',skiprows=1):
    try: 
        return np.loadtxt(fn,skiprows=skiprows).T
    except ValueError:
        return rb(fn,skiprows)

def rb(fn,skiprows):
    lines = open(fn,'r').readlines()[skiprows:]
    nrow = len(lines[0].split())
    ncol = 0

    i = 0
    D = []
    while True:
        try:
            dat = map(float,lines[i].split())
        except ValueError: pass
        except IndexError: break
        else:
            if len(dat)!=0:
                D.append(dat)
            elif len(dat)==0: break
        i = i + 1
    return np.array(D).T
