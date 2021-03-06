import csv
import os
from Process import Process
from operator import attrgetter
from math import ceil


class Simsched_Analysis(object):
    def __init__(self, _p_list, _sched_name, config):
        self.plist_config = config.name
        self.sched_name = _sched_name
        self.plist = _p_list
        self.sim_stats = Sim_stats()
        self.plist_len = len(self.plist)

    # ANALYZER FUNCTIONS

    # Average wait time for scheduler simulation. Sum total of
    # queue wait times for all processes divided by the sum total
    # of the total number of times each process waited for the CPU.
    def get_avg_wait_time(self):
        qwt = 0
        ct = 0

        for proc in self.plist:
            for i in range(1, len(proc.cpu_arrival)):
                qwt += proc.cpu_arrival[i] - proc.cpu_arrival[i-1]
            ct += (len(proc.cpu_arrival))
            qwt += (proc.start_time - proc.instantiation_time)
        avg = qwt/ct
        return avg

    # Turnaround time = Finish time - Arrival time
    def get_turnaround_times(self):
        tts = []
        for i in range(0, self.plist_len):
            tts.append(self.plist[i].finish_time -
                       self.plist[i].instantiation_time
                       )
        return tts


    def get_turnaround_over_sz(self):
        tos = []
        for i, x in enumerate(self.get_turnaround_times()):
            tos.append(ceil(x / self.plist[i].required_cpu_time))
        return tos

    #Average queue length for the entire simulation
    def get_avg_sim_queue_len(self):
        sum_lengths = 0
        sum_fetch_counts = 0
        for i in range(0, self.plist_len):
            sum_lengths += sum(self.plist[i].queue_lens)
            sum_fetch_counts += self.plist[i].fetch_count
        return ceil(sum_lengths/sum_fetch_counts)

    # list of average queue lengths for each process
    def get_avg_proc_qlens(self):
        avg_qlens = []
        for i in range(0, self.plist_len):
            avg_qlens.append(round(sum(self.plist[i].queue_lens)/self.plist[i].fetch_count, 1))
        return avg_qlens

    # List of response times for each process
    def get_response_times(self):
        response_times = []
        for i in range(0, self.plist_len):
            response_times.append(self.plist[i].start_time - self.plist[i].instantiation_time)
        return response_times

    # Average response time for simulation
    def avg_response_time(self):
        return sum(self.get_response_times())/self.plist_len

    # Process start times
    def get_start_times(self):
        start_times = []
        for i in range(0, self.plist_len):
            start_times.append(self.plist[i].start_time)
        return start_times

    # Generates list of Arrival/Instantiation times
    def get_instantiation_times(self):
        itimes = []
        for i in range(0, self.plist_len):
            itimes.append(self.plist[i].instantiation_time)
        return itimes

    # Generates list of finish times
    def get_finish_times(self):
        ftimes = []
        for i in range(0, self.plist_len):
            ftimes.append(self.plist[i].finish_time)
        return ftimes

    #Generates list of required cpu times
    def get_cpu_runtimes(self):
        rts = []
        for i in range(0, self.plist_len):
            rts.append(self.plist[i].required_cpu_time)
        return rts

    # Generates list of pids
    def get_pids(self):
        pids = []
        for i in range(0, self.plist_len):
            pids.append(self.plist[i].pid)
        return pids

    # Generates list of process sizes tiny: 0-50, small: 50-200, large: 200-1000
    def get_proc_sizes(self):
        sizes = []
        for i in range(0, self.plist_len):
            if self.plist[i].required_cpu_time > 200:
                sizes.append('LARGE')
            elif self.plist[i].required_cpu_time > 50:
                sizes.append('SMALL')
            else:
                sizes.append('TINY')
        return sizes

    # This is the sum of all required cpu times divided by total sim time.
    # In the report we refer to it as efficiency.
    def get_throughput(self):
        sum_cpu_time = 0
        for i in range(0, self.plist_len):
            sum_cpu_time += self.plist[i].required_cpu_time
        sim_time = self.plist[self.plist_len - 1].finish_time
        #finish time of last process is total simulation time
        throughput = sum_cpu_time/sim_time
        return throughput

    # Aggregates data into results container.
    def get_sim_stats(self):
        sim_stats = self.sim_stats
        sim_stats.config_name = self.plist_config
        sim_stats.sched_name = self.sched_name
        sim_stats.avg_qwts = self.get_avg_wait_time()
        sim_stats.turnaround_times = self.get_turnaround_times()
        sim_stats.avg_queue_len = self.get_avg_sim_queue_len()
        sim_stats.avg_proc_qlens = self.get_avg_proc_qlens()
        sim_stats.response_times = self.get_response_times()
        sim_stats.instantiation_times = self.get_instantiation_times()
        sim_stats.start_times = self.get_start_times()
        sim_stats.finish_times = self.get_finish_times()
        sim_stats.required_cpu_times = self.get_cpu_runtimes()
        sim_stats.pids = self.get_pids()
        sim_stats.turnaround_div_rt = self.get_turnaround_over_sz()
        sim_stats.proc_sizes = self.get_proc_sizes()
        sim_stats.throughput = self.get_throughput()
        sim_stats.avg_queue_len = self.get_avg_sim_queue_len()
        sim_stats.avg_response_time = self.avg_response_time()

        for i in range(0, len(sim_stats.start_times)):
            sim_stats.plist_config_rpt.append(sim_stats.config_name)
            sim_stats.sched_name_rpt.append(sim_stats.sched_name)
            sim_stats.throughput_rpt.append(sim_stats.throughput)
            sim_stats.avg_queue_len_rpt.append(sim_stats.avg_queue_len)
            sim_stats.avg_response_time_rpt.append(sim_stats.avg_response_time)
            sim_stats.avg_qwts_rpt.append(sim_stats.avg_qwts)

        return sim_stats

    @staticmethod
    def create_results_csv(sim_stats):
        st = sim_stats
        with open('sim_stats.csv', 'w') as csvfile:
            stat_writer = csv.writer(csvfile, quotechar='|', quoting=csv.QUOTE_MINIMAL)
            csv_fmt = Simsched_Analysis.all_vals(sim_stats, csvfile)
            for i in range(0, len(csv_fmt)):
                stat_writer.writerow(csv_fmt[i])

        Simsched_Analysis.transpose_csv('sim_stats.csv')

    # Create results file for single scheduler
    @staticmethod
    def create_results_file(sim_stats):
        st = sim_stats
        filename = 'CSV_Data/' + sim_stats.config_name + '_' + sim_stats.sched_name + '_stats.csv'
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w') as csvfile:
            stat_writer = csv.writer(csvfile, quotechar='|', quoting=csv.QUOTE_MINIMAL)
            stat_writer.writerow(["pids"] + st.pids)
            stat_writer.writerow(["instantiation times"] + st.instantiation_times)
            stat_writer.writerow(["start times"] + st.start_times)
            stat_writer.writerow(["finish times"] + st.finish_times)
            stat_writer.writerow(["average wait times"] + st.avg_qwts_rpt)
            stat_writer.writerow(["turnaround times"] + st.turnaround_times)
            stat_writer.writerow(["average queue lengths"] + st.avg_proc_qlens)
            stat_writer.writerow(["response times"] + st.response_times)
            stat_writer.writerow(["required cpu times"] + st.required_cpu_times)
            stat_writer.writerow(["process sizes"] + st.proc_sizes)
            stat_writer.writerow(["turnaround times"] + st.turnaround_div_rt)
            stat_writer.writerow(["efficiency"] + [st.throughput])
            stat_writer.writerow(["average response time"] + [st.avg_response_time])
            stat_writer.writerow(["average queue length"] + [st.avg_queue_len])
        Simsched_Analysis.transpose_csv('CSV_Data/' + sim_stats.config_name +
                                        '_' + sim_stats.sched_name + '_stats.csv')

    # Create csv file of all aggregated results
    @staticmethod
    def all_vals(sim_stats, csvfile):

        csv_fmt = [["plist configuration"],
                        ["scheduler"],
                        ["pids"],
                        ["instantiation times"],
                        ["start_times"],
                        ["finish times"],
                        ["average wait times"],
                        ["turnaround times"],
                        ["average queue lengths"],
                        ["response times"],
                        ["required cpu time"],
                        ["process sizes"],
                        ["turnaround stat"],
                        ["efficiency"],
                        ["average response time"],
                        ["average queue length"]]

        for i in range(0, len(csv_fmt)):
            for j in range(0, len(sim_stats)):
                if i == 0:
                    csv_fmt[i] += (sim_stats[j].plist_config_rpt)
                elif i == 1:
                    csv_fmt[i] += (sim_stats[j].sched_name_rpt)
                elif i == 2:
                    csv_fmt[i] += (sim_stats[j].pids)
                elif i == 3:
                    csv_fmt[i] += (sim_stats[j].instantiation_times)
                elif i == 4:
                    csv_fmt[i] += (sim_stats[j].start_times)
                elif i == 5:
                    csv_fmt[i] += (sim_stats[j].finish_times)
                elif i == 6:
                    csv_fmt[i] += (sim_stats[j].avg_qwts_rpt)
                elif i == 7:
                    csv_fmt[i] += (sim_stats[j].turnaround_times)
                elif i == 8:
                    csv_fmt[i] += (sim_stats[j].avg_proc_qlens)
                elif i == 9:
                    csv_fmt[i] += (sim_stats[j].response_times)
                elif i == 10:
                    csv_fmt[i] += (sim_stats[j].required_cpu_times)
                elif i == 11:
                    csv_fmt[i] += (sim_stats[j].proc_sizes)
                elif i == 12:
                    csv_fmt[i] += (sim_stats[j].turnaround_div_rt)
                elif i == 13:
                    csv_fmt[i] += (sim_stats[j].throughput_rpt)
                elif i == 14:
                    csv_fmt[i] += (sim_stats[j].avg_response_time_rpt)
                elif i == 15:
                    csv_fmt[i] += (sim_stats[j].avg_queue_len_rpt)
        return csv_fmt

    @staticmethod
    def transpose_csv(filename):
        with open(filename) as f:
            reader = csv.reader(f)
            cols = []
            for row in reader:
                cols.append(row)
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            for i in range(len(max(cols, key=len))):
                writer.writerow([(c[i].strip() if i<len(c) else '') for c in cols])

# Container for scheduler simulation data.
# RPT extensions are just for compiling csv files
class Sim_stats(object):
    def __init__(self):
        self.config_name = ""
        self.sched_name = ""
        self.throughput = 0
        self.throughput_rpt = []
        self.avg_response_time = 0
        self.avg_response_time_rpt = []
        self.pids = []
        self.start_times = []
        self.plist_config_rpt = []
        self.sched_name_rpt = []
        self.avg_qwts = 0
        self.avg_qwts_rpt = []
        self.turnaround_times = []
        self.avg_queue_len = 0
        self.avg_queue_len_rpt = []
        self.avg_proc_qlens = []
        self.response_times = []
        self.instantiation_times = []
        self.start_times = []
        self.finish_times = []
        self.required_cpu_times = []
        self.proc_sizes = []
        self.turnaround_div_rt = []



