from Process import P_State

class Sched_base(object):
    def __init__(self, _time_slice):
        self.name = ""
        self.time_slice = _time_slice
        self.ready_list = []
        self.empty = True

    @classmethod
    def put_process(self, proc):
        raise NotImplementedError

    @classmethod
    def fetch_process(self):
        raise NotImplementedError

    def queue_len(self):
        return len(self.ready_list) + 1

    def switch_to_ready(self, proc, SIMTIME):
        proc.cpu_arrival.append(SIMTIME)
        proc.cpu_time_remaining -= proc.time_slice
        proc.p_budget -= proc.time_slice  # for MLFQ
        proc.p_state = P_State.READY
        proc.next_state = P_State.RUNNING

    def switch_to_run(self, proc, SIMTIME):
        if proc.p_state == P_State.CREATED:
            proc.start_time = SIMTIME

        if (proc.cpu_time_remaining - proc.time_slice) <= 0:
            proc.total_runtime = proc.total_runtime + proc.cpu_time_remaining
            proc.cpu_arrival.append(SIMTIME)
            proc.finish_time = SIMTIME + proc.cpu_time_remaining
            SIMTIME += proc.cpu_time_remaining + 1
            proc.cpu_time_remaining = 0
            proc.p_state = P_State.ZOMBIE
            proc.next_state = P_State.FINISHED
        else:
            SIMTIME += proc.time_slice + 1
            proc.next_state = P_State.READY
            proc.total_runtime += proc.time_slice
            proc.p_state = P_State.RUNNING

        return SIMTIME