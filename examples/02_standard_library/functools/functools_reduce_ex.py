"""
functools 라이브러리에서 제공하는 reduce 함수는 시퀀스(리스트, 튜플 등)의 원소들을 누적적으로 특정 함수에 적용하여 단일 결과값을 생성합니다. 이 함수는 두 개의 인자를 받는 함수와 시퀀스를 인자로 받으며, 시퀀스의 원소들을 왼쪽부터 오른쪽으로 함수에 차례대로 적용합니다.

reduce는 파이썬 3에서는 기본 내장 함수가 아니므로 functools 모듈에서 명시적으로 가져와야 합니다.

다음은 reduce를 사용하는 예제입니다. 이 예제에서는 숫자 리스트의 모든 요소를 곱하는 간단한 작업을 수행합니다:

reduce 함수는 multiply 함수를 numbers 리스트의 첫 번째와 두 번째 요소에 적용하여 시작합니다. 그런 다음, 결과와 다음 요소를 multiply 함수에 적용합니다. 이 과정은 리스트의 모든 요소에 대해 수행됩니다.
"""


from functools import reduce

def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4, 5]

result = reduce(multiply, numbers)
print(result)  # 출력: 120 (1*2*3*4*5의 결과)
