#!/usr/bin/env python3

def is_safe(i, prev):
    if i == 0:
        if '^' == prev[i+1] == prev[i]:
            return False
        if '^' == prev[i+1] and '.' == prev[i]:
            return False
    elif i == len(prev)-1:
        if '^' == prev[i-1] == prev[i]:
            return False
        if '^' == prev[i-1] and '.' == prev[i]:
            return False
    else:
        if '^' == prev[i-1] == prev[i] and '.' == prev[i+1]:
            return False
        if '^' == prev[i+1] == prev[i] and '.' == prev[i-1]:
            return False
        if '^' == prev[i-1] and '.' == prev[i] == prev[i+1]:
            return False
        if '^' == prev[i+1] and '.' == prev[i] == prev[i-1]:
            return False
    return True
prev = "^.^^^.^..^....^^....^^^^.^^.^...^^.^.^^.^^.^^..^.^...^.^..^.^^.^..^.....^^^.^.^^^..^^...^^^...^...^."
count = 0
for c in prev:
    if c == '.':
        count += 1

for i in range(40-1):
    new = ''
    for j in range(len(prev)):
        if is_safe(j, prev):
            new += '.'
            count += 1
        else:
            new += '^'
    prev = new
print(count)