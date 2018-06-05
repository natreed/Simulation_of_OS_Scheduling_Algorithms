from Process import P_State
from FCFS import FCFS
from CFS import CFS
from RoundRobin import RR
from MLFQ import MLFQ
from SJF import SJF
from plist_generator import build_procs_data, plist_gen, plist_rt_spec
from Results_Analysis import Simsched_Analysis, Sim_stats
import copy


TIMESLICE = 10

if __name__ == '__main__':
    schedulers = [FCFS(TIMESLICE), CFS(TIMESLICE), MLFQ(TIMESLICE), RR(TIMESLICE), SJF(TIMESLICE)]
    sim_stats = []
    for config in plist_rt_spec:
        plist = plist_gen(build_procs_data(config))
        for scheduler in schedulers:
            proc_stats = scheduler.run(copy.deepcopy(plist))
            analyzer = Simsched_Analysis(proc_stats, scheduler.name, config)
            st = analyzer.get_sim_stats()
            sim_stats.append(st)
            analyzer.create_results_file(st)

    analyzer.create_results_csv(sim_stats)

    print("Hello")