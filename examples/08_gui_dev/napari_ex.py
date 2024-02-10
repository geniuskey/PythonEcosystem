import napari
from skimage import data

# 샘플 데이터 불러오기
astronaut = data.astronaut()
viewer = napari.view_image(astronaut, rgb=True)

napari.run()
