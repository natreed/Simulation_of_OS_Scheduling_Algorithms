import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns; sns.set(style="ticks", color_codes=True)



# Read dataset
df = pd.read_csv('sim_stats.csv')

g = sns.lmplot(x='pids',
                   y='total wait times',
                   hue='scheduler',
                   data=df,
                   size=8,
                   #palette= sns.xkcd_palette(colors)
                   )
plt.savefig('Plots/pids_x_total_wait_y_500-100k')



g = sns.factorplot(x='plist configuration',
                   y='average queue lengths',
                   hue='scheduler',
                   data=df,
                   size=8,
                   kind="bar",
                   #palette= sns.xkcd_palette(colors)
                   )
plt.savefig('Plots/config_x_avg_queue_lens_y')

g = sns.lmplot(x='pids',
                   y='turnaround stat',
                   data = df,
                   hue ='scheduler',
                   col='process sizes',
                   legend=False,
                   #palette= sns.xkcd_palette(colors)
                   )
g.despine(left=True)
plt.legend(loc='upper right')
plt.savefig('Plots/pids_x_turnaround_stat_y')


g = sns.lmplot(x='required cpu time',
                   y='turnaround times',
                   data = df,
                   hue ='scheduler',
                   legend=False,
                   sharex=False,
                   sharey=False,
                   #palette= sns.xkcd_palette(colors)
                   )
g.despine(left=True)
plt.legend(loc='upper right')
plt.savefig('Plots/cpu_time_x_turnaround_time_y')


g = sns.factorplot(x='scheduler',
                   y='average response time',
                   data=df,
                   size=8,
                   kind="bar",
                   #palette= sns.xkcd_palette(colors)
                   )
plt.savefig('Plots/average_response_time_hist')


g = sns.factorplot(x='scheduler',
                   y='throughput',
                   data=df,
                   size=8,
                   kind="bar",
                   #palette= sns.xkcd_palette(colors)
                   )
plt.savefig('Plots/throughput')

g = sns.factorplot(x='scheduler',
                   y='average queue length',
                   hue='scheduler',
                   data=df,
                   size=8,
                   kind="bar",
                   #palette= sns.xkcd_palette(colors)
                   )
plt.savefig('Plots/avg_queue_lengths')

g = sns.lmplot(x='required cpu time',
                   y='turnaround stat',
                   data=df,
                   hue='scheduler',
                   col='process sizes',
                   sharex=False,
                   sharey=False,
                   #palette= sns.xkcd_palette(colors)
                   )
plt.savefig('Plots/cpu_time_x_turnaround_stat_y')

g = sns.lmplot(x='start_times',
                   y='finish times',
                   data = df,
                   hue ='scheduler',
                   col='process sizes',
                   sharex=False,
                   sharey=False,
                   legend=False,
                   #palette= sns.xkcd_palette(colors)
                   )
g.despine(left=True)
plt.legend(loc='upper right')
plt.savefig('Plots/start_times_v_finish_times')




