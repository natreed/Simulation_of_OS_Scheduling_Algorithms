from Process import P_State,  Process

#TODO: implement blocking


running_proc = None
time_slice = 10
finished_list = []


def switch_to_ready(proc):
    global time_slice, running_proc
    if proc.p_state == P_State.RUNNING:
        proc.cpu_time_remaining -= time_slice
        running_proc = None

    next_state = P_State.READY

def switch_to_run(proc):
    global running_proc, time_slice
    running_proc = proc
    current_time = running_proc.

    if (proc.cpu_time_remaining - time_slice) <= 0:
        proc.cpu_runtime = proc.start_time + proc.cpu_time_remaining
        proc.next_state = P_State.FINISHED
        finished_list.append(proc)
    else:
        proc.next_state = P_State.READY

    return proc


def run_simulation(proc_list, scheduler):
    global running_proc, time_slice
    process_ct = len(proc_list)
    while len(proc_list > 0):
        next_proc = proc_list.pop(0)
        scheduler.empty = True

        if next_proc.next_state == P_State.READY:
            p = switch_to_ready(next_proc)
            p.p_state = P_State.READY
            scheduler.put_process(p)
            scheduler.empty = False
        elif next_proc.next_state == P_State.RUNNING:
            p = switch_to_run(next_proc)
            p.p_state = P_State.RUNNING
            scheduler.put_process(p)
            scheduler.empty = False
        elif next_proc.next_state == P_State.FINISHED:
            p = next_proc
            p.turnaround_time = p.finish_time - p.instantiation_time
            p.p_state = P_State.FINISHED
            scheduler.empty = False
            running_proc = None

        if running_proc != None or scheduler.empty == True:
            continue

        running_proc = scheduler.fetch_process()

        if running_proc == None:
            continue
        
        proc_to_add = running_proc
        proc_to_add.p_state, proc_to_add.next_state = P_State.READY, P_State.RUNNING
        scheduler.put_process(proc_to_add)
     

""" 
 current_running_process.cpu_waiting_time += current_time - current_running_process.entry_time
        current_running_process.entry_time = current_time
        new_event = Event(current_time, current_running_process, State.READY, Transition.RUN)
        event_manager.put_event(new_event)
        current_running_process = None
    return total_io_time
"""
