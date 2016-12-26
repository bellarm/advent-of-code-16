#!/usr/bin/env python3

import sys, re

lines = [line.rstrip() for line in sys.stdin]
regs = {'a': 12, 'b': 0, 'c': 0, 'd': 0}
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
    elif lines[i].startswith('tgl'):
        info = lines[i].split()
        num_ins = i+int(regs[info[1]])
        if num_ins >= len(lines):
            i += 1
            continue
        to_change = lines[num_ins].split()
        if len(to_change) == 2:
            if to_change[0] == 'inc':
                lines[num_ins] = 'dec '+to_change[1]
            else:
                lines[num_ins] = 'inc '+to_change[1]
        else:
            if to_change[0] == 'jnz':
                lines[num_ins] = 'cpy '+to_change[1]+' '+to_change[2]
            else:
                lines[num_ins] = 'jnz '+to_change[1]+' '+to_change[2]
        i += 1

print(regs['a'])