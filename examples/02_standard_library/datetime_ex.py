import datetime

# 현재 날짜와 시간
now = datetime.datetime.now()
print("Current date and time:", now)

# 특정 날짜 생성
some_date = datetime.date(2020, 1, 30)
print("Specific date:", some_date)

# 날짜와 시간 간격 계산 (timedelta)
ten_days_later = now + datetime.timedelta(days=10)
print("Ten days from now:", ten_days_later)

# 날짜 포맷팅
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", formatted_date)

# 문자열로부터 날짜 파싱
date_from_string = datetime.datetime.strptime("2024-01-15", "%Y-%m-%d")
print("Parsed date from string:", date_from_string)