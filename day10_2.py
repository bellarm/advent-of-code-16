#!/usr/bin/env python3
import sys, re, time

lines = [line.rstrip() for line in sys.stdin]
# index 0 for lo and 1 for hi value
bots_value = [[0 for i in range(2)] for j in range(210)]
out = []

def assign_value(bot, val):
    global bots_value
    if bots_value[bot][0] == 0:
        bots_value[bot][0] = val
    elif bots_value[bot][0] > val:
        bots_value[bot][1] = bots_value[bot][0]
        bots_value[bot][0] = val
    else:
        bots_value[bot][1] = val

while len(lines):
    for line in lines:
        # assign value to bot
        if re.match(r'^value', line):
            bot = int(line.split(' ')[5])
            val = int(line.split(' ')[1])
            assign_value(bot, val)
            lines.remove(line)
        bot = int(line.split(' ')[1])
        if bots_value[bot][0] == 0 or bots_value[bot][1] == 0:
            continue
        low_to = line.split(' ')[5]
        low = int(line.split(' ')[6])
        hi_to = line.split(' ')[10]
        hi = int(line.split(' ')[11])
        if low_to == "bot":
            assign_value(low, bots_value[bot][0])
            bots_value[bot][0] = 0
        elif low_to == "output" and low < 3:
            out.append(bots_value[bot][0])
            bots_value[bot][0] = 0
        if hi_to == "bot":
            assign_value(hi, bots_value[bot][1])
            bots_value[bot][1] = 0
        elif hi_to == "output" and hi < 3:
            out.append(bots_value[bot][1])
            bots_value[bot][1] = 0
        lines.remove(line)
print(out)
print(out[0]*out[1]*out[2])