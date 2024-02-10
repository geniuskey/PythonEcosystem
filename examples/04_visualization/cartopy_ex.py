import matplotlib.pyplot as plt
import cartopy.crs as ccrs

fig = plt.figure()
# 지도 투영 설정
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.set_global()

ax.coastlines()  # 해안선 추가
ax.stock_img()  # 지도 색 추가

plt.show()
