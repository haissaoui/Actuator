# Importing libraries
import numpy as np


# TVM function where FV is unknown:
def tvm_unknown_fv(n, iy, pv, pmt):
    fv = -(pv * (1 + iy) ** n + pmt * ((1 + iy) ** n - 1) / iy)
    return fv


# TVM function where PV is unknown:
def tvm_unknown_pv(n, iy, pmt, fv):
    pv = -(fv * (1 / (1 + iy)) ** n + pmt * ((1 - (1 / (1 + iy)) ** n) / iy))
    return pv


# TVM function where PMT is unknown:
def tvm_unknown_pmt(n, iy, pv, fv):
    pmt = (-fv - pv * (1 + iy) ** n) / (((1 + iy) ** n - 1) / iy)
    return pmt


# TVM function where n is unknown:
def tvm_unknown_n(iy, pv, pmt, fv):
    n = np.log((fv + pmt / iy) / (pv + pmt / iy)) / np.log(1 + iy)
    return n
