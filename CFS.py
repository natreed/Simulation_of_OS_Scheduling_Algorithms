from Sched_baseclass import Sched_base
from math import ceil

CFS_TIMESLICE = 10

class CFS(Sched_base):
    def __init__(self, _time_slice):
        super().__init__(_time_slice)
        self.name = "CFS"

    # TODO: Latency for put and fetch operations not accounted for
    # what to do for O(1) vs O(logn) data structures?
    def put_process(self, new_proc):
        if len(self.ready_list) == 0:
            new_proc.time_slice = self.time_slice
            self.ready_list.append(new_proc)
            self.empty = False
            return

        nptsl = ceil(self.time_slice / (len(self.ready_list) + 1))
        new_proc.time_slice = nptsl

        for i, process in enumerate(self.ready_list):
            if process.total_runtime > new_proc.total_runtime:
                self.ready_list.insert(i, new_proc)
                return
        self.ready_list.append(new_proc)
        return

    def fetch_process(self):
        length = len(self.ready_list)
        if length == 0:
            self.empty = True
            return None
        return self.ready_list.pop(0)


