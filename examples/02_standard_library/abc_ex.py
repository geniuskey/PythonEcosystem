from abc import ABC, abstractmethod

class AbstractAnimal(ABC):

    @abstractmethod
    def speak(self):
        pass

class Dog(AbstractAnimal):
    def speak(self):
        return "Woof!"

class Cat(AbstractAnimal):
    def speak(self):
        return "Meow!"

# 추상 클래스를 상속받은 구체 클래스의 인스턴스 생성
dog = Dog()
print(dog.speak()) # 출력: Woof!

cat = Cat()
print(cat.speak()) # 출력: Meow!

# 추상 클래스 직접 인스턴스화 시도 (오류 발생)
try:
    animal = AbstractAnimal()
except TypeError as e:
    print(e)  # Cannot instantiate abstract class AbstractAnimal with abstract method speak
