import enum

#States that a
class P_State(enum.Enum):
    CREATED = 0
    READY = 1
    RUNNING = 2
    BLOCKED = 3
    FINISHED = 4

#TODO: Could include a blocking timeout. To keep it simple
#starting with only required cpu time.
#The process is just the state of the process. The scheduler
#will make changes as necessary to the process state
class Process(object):
    def __init__(self, _start_delay, _required_cpu_time, pid):
        self.pid = pid

        self.p_state = P_State.CREATED
        self.next_state = P_State.READY
        self.required_cpu_time = _required_cpu_time
        self.cpu_time_remaining = _required_cpu_time
        self.start_delay = _start_delay
        self.intantiation_time = 0
        self.finish_time = 0
        self.cpu_runtime = 0
        self.total_runtime = 0
        self.cpu_wait_time = 0


"""class Event(object):
    def __init__(self, timestamp, process, curr_state, new_state):
        self.timestamp = timestamp
        self.process = process
        self.current_state = curr_state
        self.transition = new_state
"""