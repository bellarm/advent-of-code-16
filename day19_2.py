#!/usr/bin/env python3

num_elves = 3001330
elves = [1]*num_elves
incld = [i for i in range(num_elves)]
found = 0
elf = 0
while True:
    cur = incld.index(elf)
    leng = len(incld)
    inc = incld[(cur + leng/2) % leng]
    elves[elf] += elves[inc]
    elves[inc] = 0
    incld.remove(inc)
    if elves[elf] == num_elves:
        print(elf+1)
        break
    if inc < cur:
        cur -= 1
    elf = incld[(cur+1) % (leng-1)]