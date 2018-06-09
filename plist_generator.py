from Process import Process
import random
from math import ceil
import enum

class plist_rt_spec(enum.Enum):
    RAND = 0
    WLONG = 1
    WSRT = 2

class build_procs_data(object):
    def __init__(self, spec):
        # list size must be even for the runtime list and the instantiation time lists to match up
        self.list_size = 500
        self.runtimes = []
        self.spec = spec
        self.instantiation_times = instantiation_times_gen(self.list_size)
        # Different proc_list possibilities
        if spec == plist_rt_spec.RAND:
            self.runtimes = random_runtimes_gen(self.list_size)
        elif spec == plist_rt_spec.WSRT:
            self.runtimes = weighted_short_runtimes_gen(self.list_size)
        elif spec == plist_rt_spec.WLONG:
            self.runtimes = weighted_long_runtimes_gen(self.list_size)


def tiny_runtimes_gen(list_size):
    tiny_runtimes = []
    for i in range(0, list_size):
        tiny_runtimes.append(random.randint(10, 50))
    return tiny_runtimes

def short_runtimes_gen(list_size):
    short_runtimes = []
    for i in range(0, list_size):
        short_runtimes.append(random.randint(50, 200))
    return short_runtimes

def long_runtimes_gen(list_size):
    long_runtimes = []
    for i in range(0, list_size):
        long_runtimes.append(random.randint(200, 1000))
    return long_runtimes

def weighted_short_runtimes_gen(list_size):
    lst = tiny_runtimes_gen(ceil(list_size/4)) + \
          short_runtimes_gen(ceil(list_size/2)) + \
          long_runtimes_gen(ceil(list_size/4))
    randomized = []
    for i in range(len(lst)):
        elem = random.choice(lst)
        lst.remove(elem)
        randomized.append(elem)
    return randomized

def weighted_long_runtimes_gen(list_size):
    lst = tiny_runtimes_gen(ceil(list_size/4)) + \
          short_runtimes_gen(ceil(list_size/4)) + \
          long_runtimes_gen(ceil(list_size/2))
    randomized = []
    for i in range(len(lst)):
        elem = random.choice(lst)
        lst.remove(elem)
        randomized.append(elem)
    return randomized

def random_runtimes_gen(list_size):
    proc_runtimes = []
    for i in range(0, list_size):
        proc_runtimes.append(random.randint(10, 1000))
    return proc_runtimes

def instantiation_times_gen(list_size):
    instantiation_times = []
    for i in range(0, list_size):
        instantiation_times.append(random.randint(0,100000))
    return sorted(instantiation_times)



# Generate Process List
def plist_gen(bpd):
    proc_list = []
    for i in range(0, bpd.list_size):
        proc_list.append(Process(bpd.runtimes[i], bpd.instantiation_times[i], i))
    return proc_list

