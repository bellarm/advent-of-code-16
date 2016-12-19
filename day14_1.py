#!/usr/bin/env python3

import hashlib
def check_next_k(i, c):
    for y in range(1, 1001):
        m = hashlib.md5()
        m.update(salt.encode()+str(i+y).encode())
        hashed = m.hexdigest()
        for j in range(len(hashed)-5):
            if c == hashed[j] == hashed[j+1] == hashed[j+2] == hashed[j+3] == hashed[j+4]:
                return True
    return False
salt = "zpqevtbw"
found_key = 0
i = 0
while True:
    found = 0
    m = hashlib.md5()
    m.update(salt.encode()+str(i).encode())
    hashed = m.hexdigest()
    for x in range(len(hashed)-2):
        if hashed[x] == hashed[x+1] == hashed[x+2]:
            found = 1
            break
    if found and check_next_k(i, hashed[x]):
        found_key += 1
    if found_key == 64:
        print(i)
        break
    i += 1