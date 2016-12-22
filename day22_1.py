#!/usr/bin/env python3
import sys
NUM_Y = 26
NUM_X = 38
used = [[0 for i in range(NUM_X)] for j in range(NUM_Y)]
avai = [[0 for i in range(NUM_X)] for j in range(NUM_Y)]
for line in sys.stdin:
    if not line.startswith('/dev'):
        continue
    info = line.split()
    [coord, x, y] = info[0].split('-')
    x = int(x[1:])
    y = int(y[1:])
    used[y][x] = int(info[2][:len(info[2])-1])
    avai[y][x] = int(info[3][:len(info[3])-1])
num_pair = 0
for a_y in range(NUM_Y):
    for a_x in range(NUM_X):
        cur_used = used[a_y][a_x]
        for b_y in range(NUM_Y):
            for b_x in range(NUM_X):
                if a_y == b_y and b_x == b_y:
                    continue
                if cur_used <= avai[b_y][b_x] and cur_used != 0:
                    num_pair += 1
print(num_pair)