#!/usr/bin/env python3
import sys, re, itertools
# left negative, right positive
def rotate(pwd, dist):
    leng = len(pwd)
    start = leng - dist
    new = ''
    for i in range(leng):
        new += pwd[(start + i) % leng]
    return new

def move(pwd, fr, to):
    new = ''
    if to > fr:
        new += pwd[0:fr]
        new += pwd[fr+1:to+1]
        new += pwd[fr]
        new += pwd[to+1:]
    else:
        new += pwd[0:to]
        new += pwd[fr]
        new += pwd[to:fr]
        new += pwd[fr+1:]
    return new

def reverse(pwd, lo, hi):
    new = pwd[0:lo]
    for i in range(hi, lo-1, -1):
        new += pwd[i]
    new += pwd[hi+1:]
    return new

final_pwd = "fbgdceah"
possible = list(map("".join, itertools.permutations('abcdefgh')))
instr = [line.rstrip() for line in sys.stdin]
for pwd in possible:
    ori = pwd
    for line in instr:
        if line.startswith("rotate b"):
            char = line.split()[6]
            dist = pwd.index(char)
            if dist >= 4:
                dist += 2
            else:
                dist += 1
            pwd = rotate(pwd, dist)
        elif line.startswith("rotate"):
            [tmp, direction, dist, tmp] = line.split()
            dist = int(dist)
            if direction == "left":
                dist = -1*dist
            pwd = rotate(pwd, dist)
        elif line.startswith("move"):
            info = line.split()
            pwd = move(pwd, int(info[2]), int(info[5]))
        elif line.startswith("reverse"):
            info = line.split()
            pwd = reverse(pwd, int(info[2]), int(info[4]))
        elif line.startswith("swap"):
            [tmp, lo_to, lo, tmp, hi_to, hi] = line.split()
            if lo_to == 'letter':
                lo = pwd.index(lo)
                hi = pwd.index(hi)
            if lo_to == 'position':
                lo = int(lo)
                hi = int(hi)
            tmp1 = pwd[lo]
            tmp2 = pwd[hi]
            pwd = re.sub(tmp2, '1', pwd)
            pwd = re.sub(tmp1, tmp2, pwd)
            pwd = re.sub('1', tmp1, pwd)
    if pwd == final_pwd:
        print(ori)
        break