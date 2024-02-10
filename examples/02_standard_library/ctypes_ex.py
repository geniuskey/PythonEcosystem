from ctypes import cdll

# C 라이브러리 로드
lib = cdll.LoadLibrary('./mathlib.so')  # 실제 사용에서는 .so 혹은 .dll 연결 필요.

# C 함수 호출
result = lib.add(4, 5)

print(result)  # 출력: 9
