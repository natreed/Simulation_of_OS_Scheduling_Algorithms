from bintrees import rbtree
from Utilities import build_procs_data, process_list_gen
from Sched_baseclass import Sched_base
from Process import P_State, Process
from math import ceil

CFS_TIMESLICE = 10

class CFS(Sched_base):
    def __init__(self, _proc_list, _full_timeslice):
        self.ready_list = _proc_list
        self.full_timeslice = _full_timeslice
        self.empty = False


    def put_process(self, new_proc):
        if len(self.ready_list) == 0:
            self.ready_list.append(new_proc)
            return
        # TODO: The algorithm says something to the effect that if p_tslice drops below 1
        # we should adjust the full time slice higher. Not sure by how much though.
        # For now use ceiling b/c we can't split tics. Possibility of lots of processes with
        # time slice of 1.
        nptsl = ceil(CFS_TIMESLICE / len(self.ready_list))

        new_proc.time_slice = nptsl

        for i, process in enumerate(self.ready_list):
            if process.total_runtime > new_proc.total_runtime:
                self.ready_list.insert(i, new_proc)
                return
        self.ready_list.append(new_proc)
        return

    def peek_next_itime(self):
        if len(self.ready_list) > 0:
            return self.ready_list[0].instantiation_time
        else:
            return -1

    def fetch_process(self):
        if len(self.ready_list) == 0:
            return None
        else:
            return self.ready_list.pop(0)





"""
procs_data = build_procs_data()
proc_list = process_list_gen(procs_data)

proc_key_values = []

for i in range(0, len(proc_list)):
    proc_key_values.append((proc_list[i].total_runtime, proc_list[i]))





rbt = rbtree.RBTree(proc_key_values)
r = rbt
"""