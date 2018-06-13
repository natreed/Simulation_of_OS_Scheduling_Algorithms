from Process import P_State

class Sched_base(object):
    def __init__(self, _time_slice):
        self.name = ""
        self.time_slice = _time_slice
        self.ready_list = []
        self.finished_list = []
        self.SIMTIME = 0
        self.empty = True

    @classmethod
    def put_process(self, proc):
        raise NotImplementedError

    @classmethod
    def fetch_process(self):
        raise NotImplementedError

    # Get overhead calculates the simtime overhead for a context switch
    # Insertion overhead varies between scheduling algorithms.
    # We use average complexity: List insertion = n/2, Tree insertion = log(n)
    @classmethod
    def get_overhead(self):
        raise NotImplementedError

    def queue_len(self):
        return len(self.ready_list)

    def peek_next_itime(self, proc_list):
        if len(proc_list) > 0:
            return proc_list[0].instantiation_time
        else:
            return -1

    def switch_to_ready(self, proc):
        proc.cpu_arrival.append(self.SIMTIME)
        # self.SIMTIME += (proc.time_slice + self.get_overhead())
        self.SIMTIME += proc.time_slice
        proc.cpu_time_remaining -= proc.time_slice
        proc.p_budget -= proc.time_slice  # for MLFQ
        proc.p_state = P_State.READY
        proc.next_state = P_State.RUNNING

    def switch_to_run(self, proc):
        self.SIMTIME += 1
        if proc.p_state == P_State.CREATED:
            proc.start_time = self.SIMTIME

        if (proc.cpu_time_remaining - proc.time_slice) <= 0:
            proc.total_runtime = proc.total_runtime + proc.cpu_time_remaining
            proc.cpu_arrival.append(self.SIMTIME)   # marked for deletion
            proc.finish_time = self.SIMTIME + proc.cpu_time_remaining
            self.SIMTIME += proc.cpu_time_remaining
            proc.cpu_time_remaining = 0
            proc.p_state = P_State.ZOMBIE
            proc.next_state = P_State.FINISHED
        else:
            proc.next_state = P_State.READY
            proc.total_runtime += proc.time_slice
            proc.p_state = P_State.RUNNING
        return self.SIMTIME


    def run(self, proc_list):
        self.SIMTIME = 0
        self.finished_list = []
        while True:
            if self.empty:
                # case empty scheduler and non_empty proc_list
                if len(proc_list) != 0:
                    new_proc = proc_list.pop(0)
                    if new_proc.instantiation_time > self.SIMTIME:
                        self.SIMTIME = new_proc.instantiation_time
                    self.put_process(new_proc)
                else:
                    # case: empty scheduler and empty proc_list
                    break
            else:
                # case non_empty proc_list, and non-empty scheduler
                while len(proc_list) > 0 and self.peek_next_itime(proc_list) <= self.SIMTIME:
                    new_proc = proc_list.pop(0)
                    self.put_process(new_proc)

            proc = self.fetch_process()

            if proc is None:
                continue

            proc.fetch_count += 1
            proc.queue_lens.append(self.queue_len())
            self.SIMTIME = self.switch_to_run(proc)

            if proc.next_state == P_State.READY:
                self.switch_to_ready(proc)
                self.put_process(proc)
            elif proc.next_state == P_State.FINISHED:
                proc.p_state = P_State.FINISHED
                self.finished_list.append(proc)

        #print(self.SIMTIME)
        #print(self.finished_list[len(self.finished_list) - 1].required_cpu_time)
        return self.finished_list