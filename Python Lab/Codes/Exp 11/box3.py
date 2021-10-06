import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="darkgrid")
df = sns.load_dataset('tips')
sns.boxplot(x="day", y="total_bill", hue="smoker", data=df, palette="Set1", width=0.5)
plt.show()