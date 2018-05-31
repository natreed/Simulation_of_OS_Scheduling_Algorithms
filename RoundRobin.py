from Sched_baseclass import Sched_base
from Process import Process, P_State

class RR(Sched_base):
    def __init__(self, _time_slice):
        super().__init__(_time_slice)
        self.name="RR"

    def put_process(self, new_proc):
        new_proc.time_slice=self.time_slice
        self.ready_list.append(new_proc)
        self.empty=False

        for i, process in enumerate(self.ready_list):
            if process.required_cpu_time > self.time_slice:
                process.cpu_time_remaining= process.required_cpu_time-new_proc.time_slice
                process.total_runtime+=self.time_slice
                #process.cpu_wait
                process.p_state= P_State.RUNNING
                process.next_state=P_State.READY

            elif process.required_cpu_time < self.time_slice:
                process.cpu_time_remaining=0
                process.finish_time+= process.required_cpu_time
                process.p_state=P_State.FINISHED
                process.next_state=P_State.FINISHED
                #implement wait time
                self.ready_list.pop(process, 0)

    def fetch_process(self):
        if len(self.ready_list) == 0:
            self.empty = True
            return None
        else:
            return self.ready_list.pop(0)
