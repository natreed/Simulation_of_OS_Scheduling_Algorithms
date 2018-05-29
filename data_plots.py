import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# Read dataset
df = pd.read_csv('LONG_CFS_stats.csv', index_col=0)

df = df.T




sns.lmplot(x='instantiation times', y='response times', data=df2)
plt.show()
print("hello")
