#!/usr/bin/env python3

import sys, re
lines = [line.rstrip() for line in sys.stdin]
x = 0
found = 0
while True:
    regs = {'a': x, 'b': 0, 'c': 0, 'd': 0}
    i = 0
    output = []
    while i < len(lines):
        if lines[i].startswith('cpy'):
            [cpy, val, reg] = lines[i].split()
            try:
                regs[reg] = int(val)
            except:
                regs[reg] = regs[val]
            i += 1
        elif lines[i].startswith('inc'):
            regs[lines[i].split()[1]] += 1
            i += 1
        elif lines[i].startswith('dec'):
            regs[lines[i].split()[1]] -= 1
            i += 1
        elif lines[i].startswith('jnz'):
            [jnz, test, jmp] = lines[i].split()
            try:
                test = int(test)
            except:
                reg = test
                test = int(regs[test])
            try:
                jmp = int(jmp)
            except:
                jmp = int(regs[jmp])
            if test == 0:
                i += 1
                continue
            if jmp >= 0:
                i += jmp
            else:
                i += jmp
        elif lines[i].startswith('out'):
            output.append(regs[lines[i].split()[1]])
            for y in range(len(output)):
                if output[y] != (y % 2):
                    found = 0
                    break
                else:
                    found = 1
            if y == len(output)-1 and y == 10:
                print(x)
                sys.exit()
            if not found:
                break
            i += 1
    x += 1