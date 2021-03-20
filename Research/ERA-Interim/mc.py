### modified by CHUYAN at March 182021; Moisture convergence

import xarray as xr
import PyNIO as Nio
import pandas as pd

times = pd.to_datetime(times)
f1   = xr.open_dataset('ei.oper.an.pl.regn128sc.2019010118', engine='pynio')
f2   = xr.open_dataset('ei.oper.an.pl.regn128uv.2019070118', engine='pynio')
f3   = xr.open_dataset('ei.oper.an.sfc.regn128sc.2019010118', engine = 'pynio')

f4   = xr.open_dataset('ei.moda.an.sfc.regn128sc.2019010100', engine = 'pynio')


f5   = xr.open_dataset('era5_monthly_averaged_2019_uv.grib',  engine= 'pynio')
print(f5.dims)
#print(f5.)

print(f5.variables)

#f4 = Nio.open_file('ei.oper.an.ml.regn128uv.2013070118')

