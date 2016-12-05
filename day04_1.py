#!/usr/bin/python3.5

import sys, re

def checksum(letters, key):
    sorted_key = [v[0] for v in sorted(letters.items(), key=lambda kv: (-kv[1], kv[0]))]
    for i in range(0,5):
        if sorted_key[i] != key[i]:
            return False
    return True

rooms = [line for line in sys.stdin]
total = 0
for room in rooms:
    fields = room.split('-')
    # key[0] -> number, key[1] -> word
    key = re.findall('\w+', fields[-1])
    letters = {}
    for field in fields[:-1]:
        for c in field:
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1
    if checksum(letters, key[1]):
        total += int(key[0])

print(total)