import jax.numpy as jnp
from jax import grad, jit, vmap

# JIT 컴파일을 사용한 함수
@jit
def f(x, y):
  return jnp.dot(x, y)

# 자동 미분
df = grad(f)

# 벡터화
x = jnp.array([1.0, 2.0, 3.0])
y = jnp.array([4.0, 5.0, 6.0])
vmap_f = vmap(f, in_axes=(0, 0))
print(vmap_f(x, y))
