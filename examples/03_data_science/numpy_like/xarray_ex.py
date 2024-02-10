import xarray as xr
import numpy as np

# DataArray 생성
data = xr.DataArray(np.random.rand(4, 3),
                    dims=('x', 'y'),
                    coords={'x': [10, 20, 30, 40], 'y': [1, 2, 3]})

# 데이터 인덱싱
print(data.loc[10, 1])
print(data.sel(x=10, y=1))

# 데이터 슬라이싱
print(data.isel(x=slice(2)))
