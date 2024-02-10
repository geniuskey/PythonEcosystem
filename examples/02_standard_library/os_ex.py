import os

# 현재 작업 디렉토리 조회
current_directory = os.getcwd()
print("Current Directory:", current_directory)

# 새 디렉토리 생성
os.mkdir("new_directory")

# 디렉토리 삭제
os.rmdir("new_directory")

# 환경 변수 조회
path = os.environ.get('PATH')
print("PATH Environment Variable:", path)

# 더미 파일을 생성하고 내용을 쓰기 모드로 엽니다.
with open('dummy.txt', 'w') as dummy_file:
    dummy_file.write('This is a dummy file.')

# 파일 이름 변경
os.rename("dummy.txt", "new_dummy.txt")

# 파일 삭제
os.remove("new_dummy.txt")

# 시스템 명령 실행
os.system("echo Hello World")
