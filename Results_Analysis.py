import csv

class Simsched_Analysis(object):
    def __init__(self, _p_list, _sched_name):
        self.sched_name = _sched_name
        self.plist = _p_list
        self.sim_stats = Sim_stats()
        self.plist_len = len(self.plist)

    # ANALYZER FUNCTIONS

    # total wait time per process
    def queue_wait_time(self, arrival_times):
        qwt = 0
        for i in range(1, len(arrival_times)):
            qwt += (arrival_times[i] - arrival_times[i - 1])

        return qwt

    # This could be one measure of fairness. We could easily analyze distribution
    # of total wait times per process. Good graph material.
    def simulation_qwts(self):
        qwts = []

        for i in range(0, len(self.plist)):
            qwts.append(self.queue_wait_time(self.plist[i].cpu_arrival))

        self.sim_stats.qwts = qwts
        return qwts

    def turnaround_times(self):
        tts = []
        for i in range(0, self.plist_len):
            tts.append(self.plist[i].finish_time - self.plist[i].start_time)
        return tts

    def get_avg_queue_len(self):
        sum_lengths = 0
        sum_fetch_counts = 0
        for i in range(0, self.plist_len):
            sum_lengths += sum(self.plist[i].queue_lens)
            sum_fetch_counts += self.plist[i].fetch_count
        return sum_lengths/sum_fetch_counts



    # contains the results
    def get_sim_stats(self):
        self.sim_stats.sched_name = self.sched_name
        self.sim_stats.qwts = self.simulation_qwts()
        self.sim_stats.turnaround_times = self.turnaround_times()
        self.sim_stats.avg_queue_len = self.get_avg_queue_len()
        sim_stats = self.sim_stats

        # TODO: add more stats
        return sim_stats

    @staticmethod
    def create_results_file(sim_stats):
        with open('sim_stats.csv', 'w') as csvfile:
            stat_writer = csv.writer(csvfile, quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for st in sim_stats:
                stat_writer.writerow([st.sched_name] + ["total wait times"] + st.qwts)
                stat_writer.writerow([st.sched_name] + ["turnaround times"] + st.turnaround_times)


class Sim_stats(object):
    def __init__(self):
        self.sched_name = ""
        self.qwts = []
        self.turnaround_times = []
        self.avg_queue_len = 0



