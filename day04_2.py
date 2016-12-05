#!/usr/bin/python3.5

import sys, re

def checksum(letters, key):
    sorted_key = [v[0] for v in sorted(letters.items(), key=lambda kv: (-kv[1], kv[0]))]
    for i in range(0,5):
        if sorted_key[i] != key[i]:
            return False
    return True

def roomname(fields, sector_id):
    i = 0
    shift = sector_id % 26
    for field in fields:
        for c in field:
            c = chr(ord(c) + shift)
            if ord(c) > ord('z'):
                c = chr(ord(c) - 26)
            sys.stdout.write(c)
        sys.stdout.write(" ")
    print(str(sector_id))

rooms = [line for line in sys.stdin]
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
        roomname(fields[:-1], int(key[0]))