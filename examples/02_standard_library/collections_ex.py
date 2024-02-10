from collections import Counter, defaultdict, OrderedDict, namedtuple, deque

# Counter 사용 예제
cnt = Counter(['apple', 'orange', 'banana', 'apple', 'orange'])
print(cnt)

# defaultdict 사용 예제
d = defaultdict(int)
d['apple'] += 1
print(d)

# OrderedDict 사용 예제
od = OrderedDict()
od['apple'] = 5
od['banana'] = 10
print(od)

# namedtuple 사용 예제
Point = namedtuple('Point', ['x', 'y'])
pt = Point(1, 2)
print(pt.x, pt.y)

# deque 사용 예제
deq = deque([1, 2, 3])
deq.appendleft(0)
deq.append(4)
print(deq)
