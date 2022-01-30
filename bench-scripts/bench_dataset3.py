#!/usr/bin/env python
from common import *

configure_network()
subprocess.run(["cmake", "."])
subprocess.run(["make"])

print("start running benchmark of datasets 3")

time.sleep(5)
subprocess.run(["bin/bench_dataset_3", os.getenv("EMP_MY_PARTY_ID"), "5000"])
copy_benchmark_result_to_log("dataset_3")
