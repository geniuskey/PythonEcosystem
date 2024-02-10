from alive_progress import alive_bar
import time

items = range(100)  # 예시로 100개의 아이템을 처리한다고 가정
with alive_bar(len(items)) as bar:  # 진행 표시줄을 생성
    for item in items:
        # 여기서 각 아이템을 처리하는 작업을 수행
        time.sleep(0.1)  # 시뮬레이션을 위한 대기
        bar()  # 진행 표시줄을 업데이트