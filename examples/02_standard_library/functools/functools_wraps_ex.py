"""
functools 라이브러리의 wraps 데코레이터는 데코레이터를 만들 때 사용되며, 데코레이터 내부에서 원래 함수의 이름, 문서 문자열(docstring), 그리고 기타 속성들을 보존하는 데 도움을 줍니다. 이는 디버깅과 같은 상황에서 유용하며, 원래 함수에 대한 정보를 손실하지 않고도 데코레이터를 사용할 수 있도록 해줍니다.

아래 예제에서는 사용자 정의 데코레이터를 만들고, 이 데코레이터 내에서 wraps를 사용하여 원래 함수의 정보를 보존하는 방법을 보여줍니다.

이 예제에서 my_decorator는 wraps를 사용하여 example 함수를 데코레이트합니다. wraps 덕분에, example 함수의 이름(__name__)과 문서 문자열(__doc__)이 wrapper 함수에 의해 숨겨지지 않고 보존됩니다.
"""
from functools import wraps

def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print('Calling decorated function')
        return f(*args, **kwargs)
    return wrapper

@my_decorator
def example():
    """Docstring for example function."""
    print('Called example function')

example()
print(example.__name__)
print(example.__doc__)
