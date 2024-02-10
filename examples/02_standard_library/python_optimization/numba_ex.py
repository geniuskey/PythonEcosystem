import numba
import numpy as np

# Numba의 JIT 데코레이터를 사용
@numba.jit
def sum_array(arr):
    total = 0
    for item in arr:
        total += item
    return total

# 큰 배열 생성
arr = np.arange(1000000)

# JIT 컴파일된 함수 실행
result = sum_array(arr)
print(result)
