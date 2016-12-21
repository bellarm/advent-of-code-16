#!/usr/bin/env python3
import hashlib, sys
def is_open(c):
    if c == 'b' or c == 'c' or c == 'd' or c == 'e' or c == 'f':
        return True
    return False

def search_path(path, x, y):
    global max_length
    if x == 3 and y == 3:
        if len(path) > max_length:
            max_length = len(path)
        return
    hashed = hashlib.md5(passcode+path.encode()).hexdigest()
    if is_open(hashed[0]) and y != 0:
        search_path(path+'U',x, y-1)
    if is_open(hashed[1]) and y != 3:
        search_path(path+'D',x, y+1)
    if is_open(hashed[2]) and x != 0:
        search_path(path+'L',x-1, y)
    if is_open(hashed[3]) and x != 3:
        search_path(path+'R',x+1, y)

passcode = "mmsxrhfx"
max_length = 0
search_path('', 0, 0)
print(max_length)