# TVM function where FV is unknown:
def tvm_unknown_fv(n, iy, pv, pmt):
    fv = pv * (1 + iy) ** n + pmt * ((1 + iy) ** n - 1) / iy
    return fv


def tvm_unknown_pv(n, iy, pmt, fv):
    pv = fv * (1 / (1 + i)) ** n + pmt * ((1 - (1 / (1 + i)) ** n) / iy)
    return pv
