#!/usr/bin/env python3

import sys
lists = [[int(i) for i in line.rstrip().split('-')] for line in sys.stdin]
ranges = []
first = 1
for ip_range in sorted(lists):
    if first:
        cur_lo = ip_range[0]
        cur_hi = ip_range[1]
        first = 0
    if ip_range[0] < cur_hi and ip_range[1] > cur_hi:
        cur_hi = ip_range[1]
    elif ip_range[0] > cur_hi:
        ranges.append((cur_lo, cur_hi))
        cur_lo = ip_range[0]
        cur_hi = ip_range[1]
ranges.append((cur_lo, cur_hi))
count = 0
for i in range(len(ranges)-1):
    count += int(ranges[i+1][0]) - int(ranges[i][1]) - 1
count += 4294967295 - int(ranges[i+1][1])
print(count)