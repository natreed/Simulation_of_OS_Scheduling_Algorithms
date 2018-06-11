from Sched_baseclass import Sched_base
from Process import P_Priority, DEFAULT_BUDGET
from math import ceil


TTP = 1500  #time to promote

class MLFQ(Sched_base):

    def __init__(self, _time_slice):
        super().__init__(_time_slice)
        self.name = "MLFQ"
        for i in range (0, len(P_Priority)):
            self.ready_list.insert(0, [])
        self.time_to_promote = TTP
        self.num_queues = len(P_Priority)

    def queue_len(self):
        return sum(list(map(lambda x: len(x),self.ready_list)))  # add 1 to match base implementation?

    def get_overhead(self):
        #return ceil(self.queue_len()/2) + 1
        return 1

    def put_process(self, new_proc):
        new_proc.time_slice = self.time_slice
        self.ready_list[0].append(new_proc)
        self.empty = False
        self.update_queues()
        self.promotion_check()

    def update_queues(self):
        #start from second to last queue and work to top queue
        for i in range(self.num_queues - 2, -1, -1):
            for j in range(0, len(self.ready_list[i])):
                if self.ready_list[i][j].p_budget <= 0:
                    self.demote(self.ready_list[i][j], i, j)

    def demote(self, proc, queue, index):
        self.ready_list[queue].pop(index)
        proc.p_priority = P_Priority(queue + 1)
        self.ready_list[proc.p_priority.value].append(proc)
        proc.p_budget = DEFAULT_BUDGET

    def promotion_check(self):
        time = self.SIMTIME
        if time >= self.time_to_promote:
            #print("promotion time!")
            for i in range(1, self.num_queues):
                for j in range (0, len(self.ready_list[i])):
                    self.ready_list[i][j].p_priority = P_Priority.ZERO
                    self.ready_list[i][j].p_budget = DEFAULT_BUDGET
                self.ready_list[0] += self.ready_list[i]
                self.ready_list[i].clear()
            self.time_to_promote += TTP

    def fetch_process(self):
        for i in range(0, self.num_queues):
        # need to check budget: if it's <= 0, need to skip
            for j in range (0, len(self.ready_list[i])):
                if self.ready_list[i][j].p_budget > 0:
                    return self.ready_list[i].pop(j)
                    #okay to leave potential processes with below
                    # budgets at head of list?  won't be scheduled
                    # and will get demoted when put is called next
        self.empty = True
        return None