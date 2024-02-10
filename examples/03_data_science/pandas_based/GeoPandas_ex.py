"""
관련 라이브러리 설치 필요!
> pip install geopandas geodatasets
"""
import geopandas as gpd
from geodatasets import get_path
import matplotlib.pyplot as plt

# 공간 데이터 파일 읽기
gdf = gpd.read_file(get_path("geoda airbnb"))

# GeoDataFrame 출력
print(gdf.columns)
print(gdf.head())

# 기본적인 데이터 시각화
gdf.plot('price_pp', legend=True)
plt.show()
