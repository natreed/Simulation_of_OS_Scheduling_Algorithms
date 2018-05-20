from Process import P_State,  Process
from FCFS import FCFS
from CFS import CFS
from Utilities import build_procs_data, process_list_gen
from time import time
import copy

#TODO: implement blocking

SIMTIME = 0
TIMESLICE = 10
def switch_to_ready(proc):
    proc.cpu_time_remaining -= proc.time_slice
    proc.p_state = P_State.READY
    proc.next_state = P_State.RUNNING

def switch_to_run(proc):
    global SIMTIME


    if proc.p_state == P_State.CREATED:
        proc.start_time = SIMTIME
    if (proc.cpu_time_remaining - proc.time_slice) <= 0:
        proc.total_runtime = proc.total_runtime + proc.cpu_time_remaining
        proc.finish_time = SIMTIME + proc.cpu_time_remaining
        SIMTIME += proc.cpu_time_remaining + 1
        proc.cpu_time_remaining = 0
        proc.p_state = P_State.ZOMBIE
        proc.next_state = P_State.FINISHED
    else:
        SIMTIME += 10
        proc.next_state = P_State.READY
        proc.total_runtime += proc.time_slice
        proc.p_state = P_State.RUNNING

def peek_next_itime(ready_list):
    if len(ready_list) > 0:
        return ready_list[0].instantiation_time
    else:
        return -1

# TODO: Latency for put and fetch operations not accounted for
# what to do for O(1) vs O(logn) data structures?
def run_simulation(proc_list, scheduler):
    global SIMTIME
    finished_list = []

    # TODO: The scheduler data structure and the run list need to be
    # kept separate
    while(scheduler.peek_next_itime() >= 0):
        if SIMTIME < scheduler.peek_next_itime():
            SIMTIME = scheduler.peek_next_itime()


        proc = scheduler.fetch_process()

        switch_to_run(proc)

        if proc.next_state == P_State.READY:
            switch_to_ready(proc)
            scheduler.put_process(proc)
        elif proc.next_state == P_State.FINISHED:
            proc.p_state = P_State.FINISHED
            finished_list.append(proc)

    return finished_list

if __name__ == '__main__':
    procs_data = build_procs_data()
    proc_list = process_list_gen(procs_data)
    scheduler = FCFS(copy.deepcopy(proc_list), TIMESLICE)
    proc_stats = run_simulation(proc_list, scheduler)
    scheduler = CFS(copy.deepcopy(proc_list), TIMESLICE)
    proc_stats = run_simulation(proc_list, scheduler)
    pstats = proc_stats

