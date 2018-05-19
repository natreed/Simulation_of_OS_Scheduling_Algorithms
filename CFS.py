from bintrees import rbtree
from Utilities import build_procs_data, process_list_gen

procs_data = build_procs_data()
proc_list = process_list_gen(procs_data)

proc_key_values = []

for i in range(0, len(proc_list)):
    proc_key_values.append((proc_list[i].instantiation_time, proc_list[i]))

rbt = rbtree.RBTree(proc_key_values)
rc = rbt