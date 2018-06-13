# Algorithm comes from the Kobus paper


from Sched_baseclass import Sched_base
import math

class CFS(Sched_base):
    def __init__(self, _time_slice):
        super().__init__(_time_slice)
        self.name = "CFS"

    # Insert based on total virtual runtime. Tree data structure was not
    # necessary to implement simulation.
    def put_process(self, new_proc):
        if len(self.ready_list) == 0:
            new_proc.time_slice = self.time_slice
            self.ready_list.append(new_proc)
            self.empty = False
            return

        nprc = self.calculate_tslice()
        new_proc.time_slice = math.ceil(nprc)

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


    # Taken from the paper on "Tuning" (Kobus)
    def calculate_tslice(self):
        # Linux default period is 20. Granularity is 4.
        sched_period = 20
        min_granularity = 4
        #num running processes
        nr_running = len(self.ready_list) + 1
        # make period large enough to have a quantum of minimum granularity
        if nr_running > sched_period/min_granularity:
            sched_period = min_granularity * nr_running
        nprc = sched_period/nr_running
        return nprc
