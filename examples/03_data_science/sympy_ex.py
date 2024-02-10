from sympy import symbols, Eq, solve

x, y = symbols('x y')
equation = Eq(2*x + 3*y, 6)
solution = solve(equation, x)
print(solution)
