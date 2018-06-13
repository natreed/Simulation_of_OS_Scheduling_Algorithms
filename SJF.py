from Sched_baseclass import Sched_base
from math import ceil

class SJF(Sched_base):
    def __init__(self, _time_slice):
        super().__init__(_time_slice)
        self.name = "SJF"
    # order processes in runque by time remaining.
    def put_process(self, new_proc):
        new_proc.time_slice = self.time_slice

        if len(self.ready_list) == 0:
            self.ready_list.append(new_proc)
            self.empty = False
            return

        for i, process in enumerate(self.ready_list):
            if process.cpu_time_remaining > new_proc.cpu_time_remaining:
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
