#!/usr/bin/env python3

import sys
lists = [[int(i) for i in line.rstrip().split('-')] for line in sys.stdin]
first = 1
for ip_range in sorted(lists):
    if first:
        cur_hi = ip_range[1]
        first = 0
    if ip_range[0] < cur_hi and ip_range[1] > cur_hi:
        cur_hi = ip_range[1]
print(cur_hi+1)