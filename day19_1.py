#!/usr/bin/env python3

num_elves = 3001330
elves = [1]*num_elves
found = 0
elf = 0
while True:
    while(elves[elf] == 0):
        elf = (elf + 1) % num_elves
    inc = (elf + 1) % num_elves
    while(elves[inc] == 0):
        inc = (inc + 1) % num_elves
    elves[elf] += elves[inc]
    elves[inc] = 0
    if elves[elf] == num_elves:
        print(elf+1)
        break
    elf = (elf + 1) % num_elves