from Process import P_State, Process
import random

def random_runtimes_gen():
    list_size = random.randint(3, 6)
    proc_runtimes = []
    for i in range(0, list_size - 1):
        proc_runtimes.append(random.randint(50, 1000))
    return proc_runtimes


def process_list_gen(proc_runtimes):
    proc_list = []
    for i in range(0, len(proc_runtimes) -1):
        proc_list.append(Process(proc_runtimes[i], i))
    return proc_list