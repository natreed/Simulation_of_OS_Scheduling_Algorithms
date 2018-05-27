class Sched_base(object):
    def __init__(self, _time_slice):
        self.name = ""
        self.time_slice = _time_slice
        self.ready_list = []
        self.empty = True

    @classmethod
    def put_process(self, proc):
        raise NotImplementedError

    @classmethod
    def fetch_process(self):
        raise NotImplementedError

    def queue_len(self):
        return len(self.ready_list) + 1
