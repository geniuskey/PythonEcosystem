import pickle

# 파이썬 객체 생성
my_dict = {"name": "Python", "version": "3.9"}

# 객체를 직렬화하여 파일에 저장
with open('data.pkl', 'wb') as file:
    pickle.dump(my_dict, file)

# 파일에서 객체를 역직렬화
with open('data.pkl', 'rb') as file:
    loaded_dict = pickle.load(file)
    print(loaded_dict) # 출력: {'name': 'Python', 'version': '3.9'}

# 커스텀 객체 직렬화 및 역직렬화
class ExampleClass:
    def __init__(self, value):
        self.value = value

obj = ExampleClass(5)

# 객체 직렬화
with open('obj.pkl', 'wb') as file:
    pickle.dump(obj, file)

# 객체 역직렬화
with open('obj.pkl', 'rb') as file:
    loaded_obj = pickle.load(file)
    print(loaded_obj.value) # 출력: 5