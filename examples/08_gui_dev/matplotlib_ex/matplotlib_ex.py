import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Sine Wave')
plt.show()
