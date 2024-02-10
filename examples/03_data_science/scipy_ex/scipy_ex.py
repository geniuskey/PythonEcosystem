from scipy.optimize import minimize

# 최적화할 함수 정의
def objective_function(x):
    return x[0]**2 + x[1]**2 + x[2]**2

# 초기 추정값
initial_guess = [1, 1, 1]

# 최적화 수행
result = minimize(objective_function, initial_guess)

print(result)
