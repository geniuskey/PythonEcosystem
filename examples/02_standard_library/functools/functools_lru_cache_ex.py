"""
lru_cache를 사용하여 피보나치 수열을 계산하는 함수의 계산 결과를 캐싱하는 예제입니다. 이는 재귀 함수의 중복 계산을 피해 성능을 크게 향상시킵니다.
"""
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# 피보나치 수열의 30번째 수를 계산
print(fibonacci(30))  # 832040
