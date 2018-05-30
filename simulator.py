from Process import P_State
from FCFS import FCFS
from CFS import CFS
from RoundRobin import RR
from MLFQ import MLFQ
from plist_generator import build_procs_data, plist_gen, plist_rt_spec
from Results_Analysis import Simsched_Analysis, Sim_stats
import copy

#TODO: implement blocking

SIMTIME = 0
TIMESLICE = 10
def switch_to_ready(proc):
    proc.cpu_arrival.append(SIMTIME)
    proc.cpu_time_remaining -= proc.time_slice
    proc.p_budget -= proc.time_slice  #for MLFQ
    proc.p_state = P_State.READY
    proc.next_state = P_State.RUNNING

def switch_to_run(proc):
    global SIMTIME

    if proc.p_state == P_State.CREATED:
        proc.start_time = SIMTIME

    if (proc.cpu_time_remaining - proc.time_slice) <= 0:
        proc.total_runtime = proc.total_runtime + proc.cpu_time_remaining
        proc.cpu_arrival.append(SIMTIME)
        proc.finish_time = SIMTIME + proc.cpu_time_remaining
        SIMTIME += proc.cpu_time_remaining + 1
        proc.cpu_time_remaining = 0
        proc.p_state = P_State.ZOMBIE
        proc.next_state = P_State.FINISHED
    else:
        SIMTIME += proc.time_slice + 1
        proc.next_state = P_State.READY
        proc.total_runtime += proc.time_slice
        proc.p_state = P_State.RUNNING


def peek_next_itime(proc_list):
    if len(proc_list) > 0:
        return proc_list[0].instantiation_time
    else:
        return -1


def get_simtime():
    return SIMTIME

def run_simulation(proc_list, scheduler):
    global SIMTIME
    SIMTIME = 0
    finished_list = []

    while True:
        proc = None
        if scheduler.empty:
            # case empty scheduler and non_empty proc_list
            if len(proc_list) != 0:
                new_proc = proc_list.pop(0)
                if new_proc.instantiation_time > SIMTIME:
                    SIMTIME = new_proc.instantiation_time
                scheduler.put_process(new_proc)

            else:
                #case: empty scheduler and empty proc_list
                break         
        else:
            # case non_empty proc_list, and non-empty scheduler
            if len(proc_list) > 0:
                loc = SIMTIME
                if peek_next_itime(proc_list) <= SIMTIME:
                    new_proc = proc_list.pop(0)
                    scheduler.put_process(new_proc)

        proc = scheduler.fetch_process()

        if proc == None:
            break

        proc.fetch_count += 1

        proc.queue_lens.append(scheduler.queue_len())
        switch_to_run(proc)

        if proc.next_state == P_State.READY:
            switch_to_ready(proc)
            scheduler.put_process(proc)
        elif proc.next_state == P_State.FINISHED:
            proc.p_state = P_State.FINISHED
            finished_list.append(proc)

    return finished_list


if __name__ == '__main__':
    schedulers = [FCFS(TIMESLICE), CFS(TIMESLICE), MLFQ(TIMESLICE, get_simtime)]
    sim_stats = []
    for config in plist_rt_spec:
        plist = plist_gen(build_procs_data(config))
        for scheduler in schedulers:
            proc_stats = run_simulation(copy.deepcopy(plist), scheduler)
            analyzer = Simsched_Analysis(proc_stats, scheduler.name, config)
            sim_stats.append(analyzer.get_sim_stats())

    analyzer.create_results_file(sim_stats)
       
    print("Hello")


