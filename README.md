# sim_sched scheduling_simulator
Compare contrast and model different scheduling algorithms in an OS simulation.

## Simulated Processes: 
In this simulation, a process is  a collection of state variables and meta-data. One of the state variables is the process state (CREATED, READY, RUNNING, ZOMBIE or FINISHED). For the purposes of this simulation, an additional state, CREATED which means ‘READY but not yet run’. This state prompts the simulator to set the the process’ start time when its state is switched to RUNNING. The BLOCKED state was excluded. Simulated processes also contain scheduling related state and other metadata that track runtime scheduler performance. 

## Scheduling related state:
**pid:**  Process pids are ordered by process instantiation time or when a process is “CREATED”.

**p_state:** The process’ current state.

**next_state:** The next state transition.

**required_cpu_time:** The total amount of cpu time needed for the process to complete.

**cpu_time_remaining:** The cpu time remaining, updated in the simulator.

**P_priority:** Priority level of a process.

**P_budget:** Amount of time remaining till the process is moved to a lower priority queue. (MLFQ)

## Runtime Metadata:
**instantiation_time:** The ‘simulator time’ the process is be placed on the scheduler’s readylist.

**start_time:** The time the process is first scheduled on the cpu.

**Response time:** Start_time - Instantiation_time

**cpu_arrivals:** A list of cpu arrival times beginning with the start times. The list is updated at runtime when a process is scheduled to the cpu and is used to track average ready list wait time for the process. 

**queue_lens:** A list of queue lengths for each time a process runs. Average queue length per process is calculated using sum(queue_lens)/length(queue_lens).

**fetch_count:** Increments every time  a process is scheduled.The sum total across all processes is divided by the sum of all the queue_lens to calculate the average queue length for the scheduler simulation.

**total_runtime:** Incremented by the amount of cpu time a process gets each time it is scheduled.

**finish_time:** The simulation clock time when the process finishes running and exits the scheduler.

## Simulation Scheduler:
All schedulers implement some structured ready list and methods of adding and removing processes from the ready list. Another functionality of a scheduler is to update process state every time the process is added to or removed from the ready list. We implement the same functionality for our schedulers ‘running’ inside the simulator.
