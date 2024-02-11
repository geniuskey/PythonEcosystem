import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

# 데이터 생성
np.random.seed(10)
X = np.random.rand(100, 1)  # 독립 변수
y = X + np.random.normal(scale=0.5, size=(100, 1))  # 종속 변수

# OLS 회귀 모델 적합
X = sm.add_constant(X)  # 상수항 추가
model = sm.OLS(y, X).fit()

# 모델 요약 출력
print(model.summary())
