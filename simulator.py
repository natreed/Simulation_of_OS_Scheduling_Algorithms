from Process import P_State
from FCFS import FCFS
from CFS import CFS
from RoundRobin import RR
from MLFQ import MLFQ
from SJF import SJF
from plist_generator import build_procs_data, plist_gen, plist_rt_spec
from Results_Analysis import Simsched_Analysis, Sim_stats
import copy


TIMESLICE = 20

if __name__ == '__main__':
    # Configure list of schedulers to be analyzed
    schedulers = [CFS(TIMESLICE), MLFQ(TIMESLICE), RR(TIMESLICE), SJF(TIMESLICE), FCFS(TIMESLICE)]
    sim_stats = []
    #for config in plist_rt_spec:

    # Outer loop through WSRT, WLONG configurations
    for config in plist_rt_spec:
        # Generate processes with randomized arrival times and runtimes
        bpd = build_procs_data(config)
        plist = plist_gen(bpd)
        # Run each scheduler on same generated processes
        for scheduler in schedulers:
            # Call run to start the scheduler. Proc stats is the list of finished processes in order
            # of finish time
            proc_stats = scheduler.run(copy.deepcopy(plist))
            analyzer = Simsched_Analysis(proc_stats, scheduler.name, config)
            st = analyzer.get_sim_stats()
            sim_stats.append(st)
            analyzer.create_results_file(st)

    analyzer.create_results_csv(sim_stats)

    print("Hello")