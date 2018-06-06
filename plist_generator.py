from Process import Process
import random
from math import ceil
import enum

class plist_rt_spec(enum.Enum):
    RAND = 0
    SHORT = 1
    LONG = 2
    # split evenly between short and long runtimes
    STOL = 3    # short runtimes go first
    LTOS = 4    # long runtimes go first

class build_procs_data(object):
    def __init__(self, spec):
        # list size must be even for the runtime list and the instantiation time lists to match up
        self.list_size = 50
        self.runtimes = []
        self.spec = spec
        self.instantiation_times = instantiation_times_gen(self.list_size)
        # Different proc_list possibilities
        if spec == plist_rt_spec.RAND:
            self.runtimes = random_runtimes_gen(self.list_size)
        elif spec == plist_rt_spec.SHORT:
            self.runtimes = short_runtimes_gen(self.list_size)
        elif spec == plist_rt_spec.LONG:
            self.runtimes = long_runtimes_gen(self.list_size)
        elif spec == plist_rt_spec.STOL:
            self.runtimes = short_to_long_runtimes_gen(self.list_size)
        elif spec == plist_rt_spec.LTOS:
            self.runtimes = long_to_short_runtimes_gen(self.list_size)


def short_runtimes_gen(list_size):
    short_runtimes = []
    for i in range(0, list_size):
        short_runtimes.append(random.randint(10, 500))
    return short_runtimes

def long_runtimes_gen(list_size):
    long_runtimes = []
    for i in range(0, list_size):
        long_runtimes.append(random.randint(1000, 5000))
    return long_runtimes

def long_to_short_runtimes_gen(list_size):
    list_size = ceil(list_size/2)
    lst = long_runtimes_gen(list_size) + short_runtimes_gen(list_size)
    return lst

def short_to_long_runtimes_gen(list_size):
    list_size = ceil(list_size/2)
    lst = short_runtimes_gen(list_size) + long_runtimes_gen(list_size)
    return lst


def random_runtimes_gen(list_size):
    proc_runtimes = []
    for i in range(0, list_size):
        proc_runtimes.append(random.randint(10, 5000))
    return proc_runtimes

def instantiation_times_gen(list_size):
    instantiation_times = []
    for i in range(0, list_size):
        instantiation_times.append(random.randint(0,5000))
    return sorted(instantiation_times)


# Generate Process List
def plist_gen(bpd):
    proc_list = []
    for i in range(0, bpd.list_size):
        proc_list.append(Process(bpd.runtimes[i], bpd.instantiation_times[i], i))
    return proc_list

