#!/usr/bin/python3.5

import hashlib

door_id = "ffykfhsq"
i = 0
found = 0
password = {}
while True:
    m = hashlib.md5()
    m.update(door_id.encode()+str(i).encode())
    hashed = m.hexdigest()
    if (hashed[0] == '0' and 
       hashed[1] == '0' and
       hashed[2] == '0' and
       hashed[3] == '0' and
       hashed[4] == '0'):
        if hashed[5] < '8' and not hashed[5] in password:
            found += 1
            password[hashed[5]] = hashed[6]
            print(hashed[5] + " " + hashed[6])
    if found == 8:
        break
    i += 1

print(password)