#!/usr/bin/env python
from common import *

configure_network()
subprocess.run(["cmake", "."])
subprocess.run(["make"])

print("running the bench_jl_varying_num_dim")

k = 41
# 41 for 100k, 44 for 200k
num_records = 100000
size_of_each_dimension = 10
print("running the case for " + str(num_records) + " entries, with k value " + str(k) + ", and each dimension has size " + str(size_of_each_dimension))

time.sleep(5)
for i in range(5):
    num_dimensions = 1 + i * 1
    write_configure_info(str(num_dimensions) + " " + str(size_of_each_dimension) + " " + str(k) + " " + str(num_records))
    subprocess.run(["bin/bench_jl", os.getenv("EMP_MY_PARTY_ID"), "5000"])
    copy_benchmark_result_to_log("bench_jl varying " + str(num_dimensions) + " " + str(size_of_each_dimension) + " " + str(k) + " " + str(num_records))