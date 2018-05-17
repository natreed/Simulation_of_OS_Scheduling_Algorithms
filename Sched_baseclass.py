from abc import abstractmethod


class Sched_base(object):
    def __init__(self, _proc_list):
        self.ds = None
        self.proc_list = _proc_list
        self.empty = True

    @classmethod
    def put_process(self, proc):
        raise NotImplementedError


    @classmethod
    def fetch_process(self):
        raise NotImplementedError