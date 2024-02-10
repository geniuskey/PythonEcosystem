import ray

# Ray 초기화
ray.init()

# Ray를 사용하여 병렬 실행할 함수를 정의
@ray.remote
def f(x):
    return x * x

# 병렬로 함수를 실행하고 결과를 가져오기
futures = [f.remote(i) for i in range(4)]
print(ray.get(futures))  # [0, 1, 4, 9] 출력
