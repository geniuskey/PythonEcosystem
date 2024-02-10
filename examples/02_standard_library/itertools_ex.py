import itertools

# count 예제: 무한 카운터
for i in itertools.count(start=10, step=2):
    if i > 20:
        break
    print(i, end=' ')  # 10 12 14 16 18 20

# chain 예제: 여러 반복 가능 객체를 연결
combined = itertools.chain('ABC', 'DEF')
print(list(combined))
['A', 'B', 'C', 'D', 'E', 'F']
# permutations 예제: 모든 가능한 순열
perms = itertools.permutations('AB', 2)
print(list(perms)) # [('A', 'B'), ('B', 'A')]

# groupby 예제: 그룹화
data = sorted([('apple', 2), ('banana', 1), ('apple', 1)], key=lambda x: x[0])
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(key, list(group)) # apple [('apple', 2), ('apple', 1)], banana [('banana', 1)]