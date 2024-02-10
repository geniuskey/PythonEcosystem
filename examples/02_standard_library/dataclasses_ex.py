from dataclasses import dataclass, asdict, astuple

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0

    def total_cost(self) -> float:
        return self.price * self.quantity

# 데이터 클래스 인스턴스 생성
product = Product(name="Coffee", price=2.99, quantity=5)

# 인스턴스 사용
print(product.name)  # Coffee
print(product.total_cost())  # 14.95

# 데이터 클래스 인스턴스를 딕셔너리로 변환
print(asdict(product))  # {'name': 'Coffee', 'price': 2.99, 'quantity': 5}

# 데이터 클래스 인스턴스를 튜플로 변환
print(astuple(product))  # ('Coffee', 2.99, 5)
