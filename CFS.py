from bintrees import rbtree
from Utilities import build_procs_data, process_list_gen
from Sched_baseclass import Sched_base
from Process import P_State, Process
from math import ceil

CFS_TIMESLICE = 10

class CFS(Sched_base):
    def __init__(self, _time_slice):
        super().__init__(_time_slice)


    # TODO: In this algorithm, the number of process in the runque must be
    # accurate for correct insertion and setting the timeslice value.
    # In other words two lists are necessary.

    def put_process(self, new_proc):
        if len(self.ready_list) == 0:
            new_proc.time_slice = self.time_slice
            self.ready_list.append(new_proc)
            self.empty = False
            return
        # TODO: The algorithm says something to the effect that if p_tslice drops below 1
        # we should adjust the full time slice higher. Not sure by how much though.
        # For now use ceiling b/c we can't split tics. Possibility of lots of processes with
        # time slice of 1.
        nptsl = 1   #nptsl (new process time slice)
        if not len(self.ready_list) < 0:
            nptsl = ceil(self.time_slice / ((len(self.ready_list) + 1)))
        new_proc.time_slice = nptsl

        for i, process in enumerate(self.ready_list):
            if process.total_runtime > new_proc.total_runtime:
                self.ready_list.insert(i, new_proc)
                return
        self.ready_list.append(new_proc)
        return

    def fetch_process(self):
        if len(self.ready_list) == 0:
            self.empty = True
            return None
        else:
            return self.ready_list.pop(0)


