from OpenDartReader import OpenDartReader

# OpenDART API 키 설정 (금융감독원에서 발급받은 API 키 필요)
api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
dart = OpenDartReader(api_key)

# 삼성전자의 최근 사업 보고서 조회
report = dart.report('005930', '사업보고서', 2020)

# 삼성전자의 연간 재무제표 조회
fs = dart.finstate('005930', 2020)

print(report)
print(fs)
