"""
아래 예제는 실제 없는 파일, 폴더에 대한 예제를 만든 것이기에 이를 실행해보기보다는 API에 대한 느낌만 가져가시길 바랍니다.
"""
import shutil

# 파일 복사
shutil.copy('source.txt', 'destination.txt')

# 디렉토리 복사
shutil.copytree('source_directory', 'destination_directory')

# 디렉토리 삭제
shutil.rmtree('remove_directory')

# 파일 이동
shutil.move('source.txt', 'destination_directory')

# 디스크 사용량 확인
total, used, free = shutil.disk_usage('/')
print("Total:", total, "Used:", used, "Free:", free)

# 파일 압축
shutil.make_archive('archive', 'zip', 'directory')

# 파일 압축 해제
shutil.unpack_archive('archive.zip', 'unpacked_directory')
