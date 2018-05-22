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
        SIMTIME += proc.time_slice
        proc.next_state = P_State.READY
        proc.total_runtime += proc.time_slice
        proc.p_state = P_State.RUNNING


def peek_next_itime(proc_list):
    if len(proc_list) > 0:
        return proc_list[0].instantiation_time
    else:
        return -1

# TODO: Latency for put and fetch operations not accounted for
# what to do for O(1) vs O(logn) data structures?
def run_simulation(proc_list, scheduler):
    global SIMTIME
    SIMTIME = 0
    finished_list = []

    # TODO: The scheduler data structure and the run list need to be
    # kept separate
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
    scheduler = FCFS(TIMESLICE)
    proc_stats = run_simulation(copy.deepcopy(proc_list), scheduler)
    scheduler = CFS(TIMESLICE)
    proc_stats = run_simulation(copy.deepcopy(proc_list), scheduler)
    pstats = proc_stats

