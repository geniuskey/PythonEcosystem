import re

# 패턴 매칭 예제
text = "The rain in Spain"
result = re.search("rain", text)
if result:
    print("Found:", result.group())

# 패턴 대체 예제
replaced_text = re.sub("Spain", "France", text)
print("Replaced Text:", replaced_text)

# 패턴 컴파일 예제
pattern = re.compile(r'\bS\w+')
matches = pattern.findall(text)
print("Words starting with 'S':", matches)

# 플래그 사용 예제
case_insensitive_search = re.search("THE", text, re.IGNORECASE)
if case_insensitive_search:
    print("Found with ignore case:", case_insensitive_search.group())

# 서브셋 추출 예제
email = "user@example.com"
match = re.search(r'(\w+)@(\w+).(\w+)', email)
if match:
    print("Username:", match.group(1)) # user
    print("Domain:", match.group(2)) # example
    print("Top-Level Domain:", match.group(3)) # com