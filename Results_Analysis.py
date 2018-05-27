import csv
from Process import Process
from operator import attrgetter

class Simsched_Analysis(object):
    def __init__(self, _p_list, _sched_name, config):
        self.plist_config = config.name
        self.sched_name = _sched_name
        self.plist = sorted(_p_list, key=attrgetter('pid'))
        self.sim_stats = Sim_stats()
        self.plist_len = len(self.plist)

    # ANALYZER FUNCTIONS

    # total wait time per process
    def get_queue_wait_time(self, arrival_times):
        qwt = 0
        for i in range(1, len(arrival_times)):
            qwt += (arrival_times[i] - arrival_times[i - 1])
        return qwt


    # This could be one measure of fairness. We could easily analyze distribution
    # of total wait times per process. Good graph material.
    def get_sim_qwts(self):
        qwts = []
        for i in range(0, len(self.plist)):
            qwts.append(self.get_queue_wait_time(self.plist[i].cpu_arrival))

        self.sim_stats.qwts = qwts
        return qwts


    def get_turnaround_times(self):
        tts = []
        for i in range(0, self.plist_len):
            tts.append(self.plist[i].finish_time - self.plist[i].start_time)
        return tts

    #Average queue length for the entire simulation
    def get_avg_sim_queue_len(self):
        sum_lengths = 0
        sum_fetch_counts = 0
        for i in range(0, self.plist_len):
            sum_lengths += sum(self.plist[i].queue_lens)
            sum_fetch_counts += self.plist[i].fetch_count
        return sum_lengths/sum_fetch_counts

    # list of average queue lengths for each process
    def get_avg_proc_qlens(self):
        avg_qlens = []
        for i in range(0, self.plist_len):
            avg_qlens.append(round(sum(self.plist[i].queue_lens)/self.plist[i].fetch_count, 1))
        return avg_qlens

    def get_response_times(self):
        response_times = []
        for i in range(0, self.plist_len):
            response_times.append(self.plist[i].start_time - self.plist[i].instantiation_time)
        return response_times

    def get_start_times(self):
        start_times = []
        for i in range(0, self.plist_len):
            start_times.append(self.plist[i].start_time)
        return start_times

    def get_instantiation_times(self):
        itimes = []
        for i in range(0, self.plist_len):
            itimes.append(self.plist[i].instantiation_time)
        return itimes

    def get_finish_times(self):
        ftimes = []
        for i in range(0, self.plist_len):
            ftimes.append(self.plist[i].finish_time)
        return ftimes


    # contains the results
    def get_sim_stats(self):
        sim_stats = self.sim_stats
        sim_stats.plist_config = self.plist_config
        sim_stats.sched_name = self.sched_name
        sim_stats.qwts = self.get_sim_qwts()
        sim_stats.turnaround_times = self.get_turnaround_times()
        sim_stats.avg_queue_len = self.get_avg_sim_queue_len()
        sim_stats.avg_proc_qlens = self.get_avg_proc_qlens()
        sim_stats.response_times = self.get_response_times()
        sim_stats.instantiation_times = self.get_instantiation_times()
        sim_stats.start_times = self.get_start_times()
        sim_stats.finish_times = self.get_finish_times()

        # TODO: add more stats
        return sim_stats

    @staticmethod
    def create_results_file(sim_stats):
        with open('sim_stats.csv', 'w') as csvfile:
            stat_writer = csv.writer(csvfile, quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for st in sim_stats:
                stat_writer.writerow([st.plist_config, st.sched_name] + ["instantiation times"] + st.instantiation_times)
                stat_writer.writerow([st.plist_config, st.sched_name] + ["start_times"] + st.start_times)
                stat_writer.writerow([st.plist_config, st.sched_name] + ["finish times"] + st.finish_times)
                stat_writer.writerow([st.plist_config, st.sched_name] + ["total wait times"] + st.qwts)
                stat_writer.writerow([st.plist_config, st.sched_name] + ["turnaround times"] + st.turnaround_times)
                stat_writer.writerow([st.plist_config, st.sched_name] + ["average queue lengths"] + st.avg_proc_qlens)
                stat_writer.writerow([st.plist_config, st.sched_name] + ["response times"] + st.response_times)
                #stat_writer.writerow([''])


class Sim_stats(object):
    def __init__(self):
        self.plist_config = ""
        self.sched_name = ""
        self.qwts = []
        self.turnaround_times = []
        self.avg_queue_len = 0
        self.avg_proc_qlens = []
        self.response_times = []
        self.instantiation_times = []
        self.start_times = []
        self.finish_times = []



