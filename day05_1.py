#!/usr/bin/python3.5

import hashlib

door_id = "ffykfhsq"
i = 0
found = 0
while True:
    m = hashlib.md5()
    m.update(door_id.encode()+str(i).encode())
    hashed = m.hexdigest()
    if (hashed[0] == '0' and 
       hashed[1] == '0' and
       hashed[2] == '0' and
       hashed[3] == '0' and
       hashed[4] == '0'):
        found += 1
        print(hashed[5])
    if found == 8:
        break
    i += 1