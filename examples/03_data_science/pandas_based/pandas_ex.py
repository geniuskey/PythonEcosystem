import pandas as pd

# 데이터 프레임 생성
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 34, 29, 32],
        'City': ['New York', 'Paris', 'Berlin', 'London']}
df = pd.DataFrame(data)

# 데이터 보기
print(df)

# 특정 조건에 맞는 데이터 필터링
filtered_df = df[df['Age'] > 30]

print(filtered_df)
