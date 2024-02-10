import time

# 현재 시간을 초 단위로 얻기
current_time = time.time()
print("Current time:", current_time)

# 프로그램을 3초간 일시 정지
time.sleep(3)

# 현재 시간을 구조화된 형태(localtime)로 변환
local_time = time.localtime()
print("Local time:", time.asctime(local_time))

# strftime을 사용하여 날짜와 시간 포맷 지정
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print("Formatted time:", formatted_time)
