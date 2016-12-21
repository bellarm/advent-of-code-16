#!/usr/bin/env python3
import sys
discs = []
for line in sys.stdin:
    info = line.rstrip().split()
    discs.append((int(info[3]), int(info[11].replace('.',''))))
discs.append((11, 0))
i = 0
found = 0
while True:
    pos = (discs[0][1]+i) % discs[0][0]
    for j in range(1,len(discs)):
        tmp = (discs[j][1]+(i+j)) % discs[j][0]
        if tmp != pos:
            break
        if j == len(discs)-1:
            found = 1
    if found:
        break
    i += 1
print(i-1)