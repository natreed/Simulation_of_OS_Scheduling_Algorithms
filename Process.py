import enum
import time



#States that a
class P_State(enum.Enum):
    CREATED = 0
    READY = 1
    RUNNING = 2
    BLOCKED = 3
    ZOMBIE = 4
    FINISHED = 5

#TODO: Could include a blocking timeout. To keep it simple
#starting with only required cpu time.
#The process is just the state of the process. The scheduler
#will make changes as necessary to the process state
class Process(object):
    def __init__(self, _required_cpu_time, _instantiation_time, _pid):
        self.pid = _pid
        self.time_slice = 0
        self.p_state = P_State.CREATED
        self.next_state = P_State.RUNNING
        self.required_cpu_time = _required_cpu_time
        self.cpu_time_remaining = _required_cpu_time
        self.start_time = 0
        self.instantiation_time = _instantiation_time
        self.finish_time = 0
        self.total_runtime = 0