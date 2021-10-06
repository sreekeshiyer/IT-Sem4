import matplotlib.pyplot as plt
import numpy as np
np.random.seed(444)
np.set_printoptions(precision=3)
d = np.random.laplace(loc=15, scale=3, size=500)
n, bins, patches = plt.hist(x=d, bins='auto', color='#0504aa',alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('My Histogram')
plt.text(23, 45, r'$\mu=15, b=3$')
maxfreq = n.max()
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
plt.show()