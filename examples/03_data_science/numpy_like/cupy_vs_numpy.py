import cupy as cp
import numpy as np
import time

n = 1000000000  # 데이터의 개수

# NumPy를 사용하여 CPU에서 데이터 생성 및 표준편차 계산
np.random.seed(0)
x_cpu = np.random.rand(n)
start_time = time.time()
std_cpu = np.std(x_cpu)
numpy_time = time.time() - start_time
print(f"NumPy (CPU) 표준편차 계산 시간: {numpy_time:.5f} 초")
print(f"NumPy 표준편차 값: {std_cpu}")

# CuPy를 사용하여 GPU에서 동일한 데이터 생성 및 표준편차 계산
cp.random.seed(0)
x_gpu = cp.random.rand(n)
start_time = time.time()
std_gpu = cp.std(x_gpu)
cupy_time = time.time() - start_time

print(f"CuPy (GPU) 표준편차 계산 시간: {cupy_time:.5f} 초")
print(f"CuPy 표준편차 값: {std_gpu}")
