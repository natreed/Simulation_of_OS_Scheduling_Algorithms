from Sched_baseclass import Sched_base

class FCFS(Sched_base):
    def __init__(self, proc_list):
        super().__init__(proc_list)
        self.ds = []
        #just a more descriptive alias in this case
        #TODO: for more complex structures it will be necessary to convert the proclist
        self.ready_list = self.ds
        self.completed = False

    def put_process(self, new_proc):
        if len(self.ready_list) == 0:
            self.queue.append(new_proc)
            return

        for i, process in enumerate(self.ready_list):
            if process.start_time > new_proc.start_time:
                self.ready_list.insert(i, new_proc)
                return

        self.ready_list.append(new_proc)
        return

    def fetch_process(self):
        if len(self.ready_list) == 0:
            return None
        else:
            return self.ready_list.pop(0)




