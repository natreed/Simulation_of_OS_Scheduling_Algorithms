# Algorithm comes from
# https://tampub.uta.fi/bitstream/handle/10024/96864/GRADU-1428493916.pdf


from Sched_baseclass import Sched_base
import math

CFS_TIMESLICE = 10

class CFS(Sched_base):
    def __init__(self, _time_slice):
        super().__init__(_time_slice)
        self.name = "CFS"

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

    def get_overhead(self):
        ml = math.log(1, 2)
        if len(self.ready_list) == 0:
            return 1
        overhead = math.ceil(math.log(len(self.ready_list), 2))
        return overhead


    def calculate_tslice(self):
        # keep burst in range 1 - 20
        while True:
            try:
                nprc = self.time_slice / (len(self.ready_list))
                if nprc >= 1 and nprc <= 20:
                    break
                if nprc < 1:
                    self.time_slice += 4
                if nprc > 20:
                    self.time_slice -= 4
            except Exception:
                print("broke")

        return nprc
