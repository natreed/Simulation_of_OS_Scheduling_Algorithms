import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns; sns.set(style="ticks", color_codes=True)


# Read dataset
df = pd.read_csv('sim_stats.csv')

g = sns.factorplot(x='plist configuration',
                   y='average queue lengths',
                   hue='scheduler',
                   data = df,
                   size = 8,
                   kind = "bar",
                   palette = "muted"
                   )
plt.show()
g = sns.factorplot(x='plist configuration',
                   y='total wait times',
                   hue='scheduler',
                   data = df,
                   size = 8,
                   kind = "bar",
                   palette = "muted"
                   )

plt.show()
g = sns.lmplot(x='instantiation times',
                   y='response times',
                   data = df,
                   hue = 'scheduler',
                   col= 'plist configuration'
                   )
plt.show()
