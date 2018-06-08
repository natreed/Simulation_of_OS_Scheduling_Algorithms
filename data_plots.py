import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns; sns.set(style="ticks", color_codes=True)


# Read dataset
df = pd.read_csv('sim_stats.csv')

g = sns.factorplot(x='scheduler',
                   y='',
                   hue='scheduler',
                   data=df,
                   size=8,
                   kind="bar",
                   palette="muted"
                   )
plt.savefig('Plots/total_wait_times_hist')
plt.show()
exit(0)

g = sns.factorplot(x='scheduler',
                   y='throughput',
                   data=df,
                   size=8,
                   kind="bar",
                   palette="muted"
                   )
plt.savefig('Plots/throughput')
plt.show()
exit(0)

g = sns.factorplot(x='process sizes',
                   y='average queue length',
                   hue='scheduler',
                   data=df,
                   size=8,
                   kind="bar",
                   palette="muted"
                   )
plt.savefig('Plots/avg_queue_lengths')
plt.show()
exit(0)

g = sns.lmplot(x='pids',
                   y='turnaround stat',
                   data = df,
                   hue ='scheduler',
                   col='process sizes',
                   sharex=False,
                   sharey=False,
                   legend=False
                   )
g.despine(left=True)
plt.legend(loc='upper right')
plt.savefig('Plots/pids_x_turnaround_stat_y')


g = sns.lmplot(x='required cpu time',
                   y='turnaround stat',
                   data=df,
                   hue='scheduler',
                   col='process sizes',
                   sharex=False,
                   sharey=False
                   )
plt.savefig('Plots/cpu_time_x_turnaround_stat_y')


g = sns.lmplot(x='required cpu time',
                   y='turnaround times',
                   data = df,
                   hue ='scheduler',
                   legend=False,
                   sharex=False,
                   sharey=False
                   )
g.despine(left=True)
plt.legend(loc='upper right')
plt.savefig('Plots/cpu_time_x_turnaround_time_y')


g = sns.factorplot(x='plist configuration',
                   y='total wait times',
                   hue='scheduler',
                   data=df,
                   size=8,
                   kind="bar",
                   palette="muted"
                   )
plt.savefig('Plots/total_wait_times_hist')


g = sns.lmplot(x='start_times',
                   y='finish times',
                   data = df,
                   hue ='scheduler',
                   col='process sizes',
                   sharex=False,
                   sharey=False,
                   legend=False
                   )
g.despine(left=True)
plt.legend(loc='upper right')
plt.savefig('Plots/start_times_v_finish_times')
plt.show()

exit(0)














g = sns.factorplot(x='plist configuration',
                   y='average queue lengths',
                   hue='scheduler',
                   data=df,
                   size=8,
                   kind="bar",
                   palette="muted"
                   )
plt.show()

