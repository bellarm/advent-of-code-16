#!/usr/bin/env python3
import hashlib, sys
def is_open(c):
    if c == 'b' or c == 'c' or c == 'd' or c == 'e' or c == 'f':
        return True
    return False

def search_path(path, x, y):
    global to_visit
    if x == 3 and y == 3:
        print(path)
        sys.exit()
    hashed = hashlib.md5(passcode+path.encode()).hexdigest()
    if is_open(hashed[0]):
        if y != 0:
            search_path(path+'U',x, y-1)
    if is_open(hashed[1]):
        if y != 3:
            search_path(path+'D',x, y+1)
    if is_open(hashed[2]):
        if x != 0:
            search_path(path+'L',x-1, y)
    if is_open(hashed[3]):
        if x != 3:
            search_path(path+'R',x+1, y)
passcode = "mmsxrhfx"
path = [['' for i in range(4)] for j in range(4)]
to_visit = [(0,0), ]
search_path(path[0][0], 0, 0)