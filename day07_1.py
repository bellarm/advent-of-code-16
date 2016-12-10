#!/usr/bin/python3.5

import sys, re

def supports_tls(ip):
    # split the ip into words, since ip never starts with []
    # so if index is odd then inside bracket
    # if index is even outside bracket
    words = ip.split(' ')
    is_in_brackets = 0
    total_pattern = 0
    for word in words:
        found_pattern = 0
        for i in range(len(word)-3):
            if word[i] == word[i+3] and word[i+1] == word[i+2] and word[i] != word[i+1]:
                found_pattern = 1
            if is_in_brackets and found_pattern:
                return False
        if is_in_brackets == 1:
            is_in_brackets = 0
        else:
            total_pattern += found_pattern
            is_in_brackets = 1
    if total_pattern == 0:
        return False
    return True
        

ips = [line for line in sys.stdin]
valid_ip = 0
for ip in ips:
    # convert all the brackets to spaces
    ip = re.sub(r'[\[\]]', ' ', ip)
    if supports_tls(ip):
        valid_ip += 1 

print(valid_ip)