import matplotlib.pyplot as plt
from adjustText import adjust_text
import numpy as np

# 샘플 데이터 생성
data_size = 40
np.random.seed(0)
x = np.random.randn(data_size)
y = np.random.randn(data_size)
texts = [plt.text(x[i], y[i], f'Point {i}') for i in range(data_size)]

# 그래프 그리기
plt.scatter(x, y)

# 텍스트 레이블 조정
adjust_text(texts)
# adjust_text(texts, arrowprops=dict(arrowstyle='->'))

# 결과 표시
plt.show()
