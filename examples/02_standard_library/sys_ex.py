import sys

# 명령줄 인자 출력
print(f"Command Line Arguments: {sys.argv}")

# Python 경로 출력
print(f"Python Path: {sys.path}")

# 표준 출력에 메시지 작성
sys.stdout.write("Hello, sys module!\n")

# Python 버전 정보 출력
print(f"Python Version: {sys.version}")

# 현재 운영 체제 플랫폼 출력
print(f"Platform: {sys.platform}")

# 스크립트 종료
sys.exit(0)