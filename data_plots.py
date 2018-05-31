import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns; sns.set(style="ticks", color_codes=True)


# Read dataset
df = pd.read_csv('sim_stats.csv')

sns.lmplot(x='instantiation times',
           y='response times',
           data=df,
           hue='scheduler',
           col='plist configuration')
plt.show()
print("hello")
