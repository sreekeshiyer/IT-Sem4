import matplotlib.pyplot as plt
import pandas as pd
wine_reviews = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)
fig, ax = plt.subplots()
ax.hist(wine_reviews['points'])
ax.set_title('Wine Review Scores')
ax.set_xlabel('Points')
ax.set_ylabel('Frequency')
plt.show()