import matplotlib.pyplot as plt
import pandas as pd
wine_reviews = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)
wine_reviews.groupby("country").price.mean().sort_values(ascending=False)[:5].plot.bar()
plt.show()