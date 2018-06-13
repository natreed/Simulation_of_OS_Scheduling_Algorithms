from Sched_baseclass import Sched_base
from math import ceil

class RR(Sched_base):
    def __init__(self, _time_slice):
        super().__init__(_time_slice)
        self.name="RR"

    def put_process(self, new_proc):
        new_proc.time_slice=self.time_slice
        self.ready_list.append(new_proc)
        self.empty=False

    def fetch_process(self):
        if len(self.ready_list) == 0:
            self.empty = True
            return None
        else:
            return self.ready_list.pop(0)

