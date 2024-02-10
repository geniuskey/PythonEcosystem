from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

# 샘플 데이터 생성
fs = 1000  # 샘플링 주파수
t = np.arange(0, 1.0, 1.0/fs)
x = np.sin(2*np.pi*5*t) + 1.5*np.sin(2*np.pi*250*t)

# 저주파 버터워스 필터 설계
b, a = signal.butter(3, 30/(0.5*fs), 'low')

# 필터 적용
filtered = signal.filtfilt(b, a, x)

# 결과 플로팅
plt.plot(t, x, label='Original')
plt.plot(t, filtered, label='Filtered')
plt.legend()
plt.show()
