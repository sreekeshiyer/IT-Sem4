import matplotlib.pyplot as plt
import numpy as np
values=np.cumsum(np.random.randn(1000,1))
plt.plot(values)
plt.show()