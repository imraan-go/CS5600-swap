#! /usr/bin/env python3
# import os

# import subprocess
import matplotlib.pyplot as plt
import numpy as np

# cacheSizes = np.arange(0, 120, 20)
cacheSizes = np.arange(1, 5)
policies = ["FIFO", "LRU", "OPT", "UNOPT", "RAND", "CLOCK"]
hitRates = [
    [54.60, 74.60, 98.40, 98.40],
    [54.60, 82.80, 98.60, 98.60],
    [54.60, 82.80, 98.60, 98.60],
    [54.60, 54.60, 57.00, 57.20],
    [54.60, 78.60, 98.20, 98.00],
    [54.60, 78.80, 98.00, 98.20]
]

# for cacheSize in cacheSizes:
#     hitRate = []
#     for policy in policies:
#         result = subprocess.run(["./paging-policy.py", "-c", "-p", policy,
#             "-f", "./vpn.txt", "-C", str(cacheSize)], stdout=subprocess.PIPE)
#         result = result.stdout.decode('utf-8')
#         hitRate.append(result)
#     hitRates.append(hitRate)

for i in range(len(policies)):
    plt.plot(cacheSizes, hitRates[i])

plt.legend(policies)
plt.margins(0)
plt.xticks(cacheSizes, cacheSizes)
plt.xlabel('Cache Size (Blocks)')
plt.ylabel('Hit Rate')
plt.savefig('workload.png', dpi=227)
