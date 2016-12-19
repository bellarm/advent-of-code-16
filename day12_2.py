#!/usr/bin/env python3

import sys, re

lines = [line.rstrip() for line in sys.stdin]
regs = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
i = 0
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
        jmp = int(jmp)
        if test == 0:
            i += 1
            continue
        if jmp >= 0:
            i += jmp
        else:
            i += jmp
print(regs)