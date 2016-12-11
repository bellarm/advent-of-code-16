#!/usr/bin/python3.5

import sys, re, time

instructions = [line for line in sys.stdin]
bots_value = [[-1 for i in range(2)] for j in range(210)]
bots_give = [[-1 for i in range(2)] for j in range(210)]

def print_stat(bot):
    print("bot: %d:" % (bot))
    print("\tlo: %d" % (bots_value[bot][0]))
    print("\thi: %d" % (bots_value[bot][1]))

def assign_value(bot, val):
    global bots_value
    if bots_value[bot][0] == -1:
        bots_value[bot][0] = val
    elif bots_value[bot][0] > val:
        bots_value[bot][1] = bots_value[bot][0]
        bots_value[bot][0] = val
    else:
        bots_value[bot][1] = val

def give_chip(bot):
    global bots_value
    global bots_give
    # base conditions
    if bots_give[bot][0] == -1 or bots_give[bot][1] == -1 or bots_value[bot][0] == -1 or bots_value[bot][1] == -1:
        return
    if bots_value[bot][0] == 17 and bots_value[bot][1] == 61:
        print(bot)
        return
    # give low
    assign_value(bots_give[bot][0], bots_value[bot][0])
    bots_value[bot][0] = -1
    to = bots_give[bot][0]
    bots_give[bot][0] = -1
    give_chip(to)
    # give high
    assign_value(bots_give[bot][1], bots_value[bot][1])
    bots_value[bot][1] = -1
    to = bots_give[bot][1]
    bots_give[bot][1] = -1
    give_chip(to)

for line in instructions:
    if re.match(r'^value', line):
        # assign value to all bots first
        bot = int(line.split(' ')[5])
        val = int(line.split(' ')[1])
        assign_value(bot, val)
    if re.match(r'^bot', line):
        # bot gives hi/lo chip to
        bot = int(line.split(' ')[1])
        low_to = line.split(' ')[5]
        low = int(line.split(' ')[6])
        hi_to = line.split(' ')[10]
        hi = int(line.split(' ')[11])
        if low_to == "bot":
            bots_give[bot][0] = low
        if hi_to == "bot":
            bots_give[bot][1] = hi
    
for bot in range(209):
    if bots_value[bot][0] != -1 and bots_value[bot][1] != -1:
        give_chip(bot)