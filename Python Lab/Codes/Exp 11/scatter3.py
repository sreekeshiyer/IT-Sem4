import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
df = pd.read_csv('AmesHousing.csv')
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
x = df['SalePrice']
y = df['Gr Liv Area']
z = df['Overall Qual']
ax.scatter(x, y, z)
ax.set_xlabel("Sale price")
ax.set_ylabel("Living area above ground level")
ax.set_zlabel("Overall quality")
plt.show()