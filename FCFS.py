from Sched_baseclass import Sched_base

class FCFS(Sched_base):
    def __init__(self, _time_slice):
        super().__init__(_time_slice)
        self.name = "FCFS"

    def put_process(self, new_proc):
        new_proc.time_slice = self.time_slice
        if len(self.ready_list) == 0:
            self.ready_list.append(new_proc)
            self.empty = False
            return

        for i, process in enumerate(self.ready_list):

            if process.pid > new_proc.pid:
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




