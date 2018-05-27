from Process import Process
import random

class build_procs_data(object):
    def __init__(self):
        self.list_size = random.randint(8,12)
        self.runtimes = random_runtimes_gen(self.list_size)
        self.instantiation_times = instantiation_times_gen(self.list_size)



def random_runtimes_gen(list_size):
    proc_runtimes = []
    for i in range(0, list_size):
        proc_runtimes.append(random.randint(5, 100))
    return proc_runtimes

def instantiation_times_gen(list_size):
    instantiation_times = []
    for i in range(0, list_size):
        instantiation_times.append(random.randint(0,20))
    return sorted(instantiation_times)

def process_list_gen(bpd):
    proc_list = []
    for i in range(0, bpd.list_size):
        proc_list.append(Process(bpd.runtimes[i], bpd.instantiation_times[i], i))
    return proc_list