from Sched_baseclass import Sched_base

class FCFS(Sched_base):
    def __init__(self, proc_list):
        super().__init__(proc_list)
        #just a more descriptive alias in this case
        #TODO: for more complex structures it will be necessary to convert the proclist
        self.ready_list = proc_list
        self.completed = False

    def put_process(self, new_proc):
        if len(self.ready_list) == 0:
            self.ready_list.append(new_proc)
            return

        for i, process in enumerate(self.ready_list):
            if process.instantiation_time > new_proc.instantiation_time:
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




