"""
partial을 사용하여 함수의 일부 인자를 고정하고, 새로운 함수를 생성하는 예제입니다. 여기서는 power 함수에 대해 밑(base)을 고정하여 새로운 square 및 cube 함수를 만듭니다.
"""
from functools import partial

def power(base, exponent):
    return base ** exponent

# 밑을 2로 고정하여 새로운 함수 생성
square = partial(power, 2)

# 밑을 3으로 고정하여 새로운 함수 생성
cube = partial(power, 3)

print(square(4))  # 16 (2의 4제곱)
print(cube(4))    # 81 (3의 4제곱)
