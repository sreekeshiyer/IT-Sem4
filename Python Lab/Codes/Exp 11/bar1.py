import matplotlib.pyplot as plt
import pandas as pd
wine_reviews = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)
fig, ax = plt.subplots() 
data = wine_reviews['points'].value_counts() 
points = data.index 
frequency = data.values 
ax.bar(points, frequency) 
ax.set_title('Wine Review Scores') 
ax.set_xlabel('Points') 
ax.set_ylabel('Frequency')
plt.show()