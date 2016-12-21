#!/usr/bin/env python3
import re
digit = "10111011111001111"
disk_length = 35651584
# dragon curve
while len(digit) < disk_length:
    reverse = digit[::-1]
    reverse = re.sub('0','a',reverse)
    reverse = re.sub('1','0',reverse)
    reverse = re.sub('a','1',reverse) 
    digit += '0'+reverse
# check sum
checksum = digit[:disk_length]
while len(checksum) % 2 != 1:
    new = ''
    for i in range(0, len(checksum), 2):
        if checksum[i] == checksum[i+1]:
            new += '1'
        else:
            new += '0'
    checksum = new
print(checksum)