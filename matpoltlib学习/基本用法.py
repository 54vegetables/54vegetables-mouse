import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, -1, 50)    # x轴从-1到1共50个点
y = 2 * x + 1
plt.plot(x, y)
plt.show()