import cupy as cp

# CuPy 배열 생성
x = cp.arange(6).reshape(2, 3)

# CuPy 배열에 대한 연산 수행
y = cp.sin(x)

print(x, y)