#!/usr/bin/python3.5

import sys, re

def support_ssl(ip):
    words = ip.split(' ')
    is_in_brackets = 0
    patterns_inside_bracket = []
    patterns_outside_bracket = []
    for word in words:
        for i in range(len(word)-2):
            if word[i] == word[i+2]:
                if is_in_brackets:
                    patterns_inside_bracket.append(word[i]+word[i+1]+word[i+2])
                else:
                    patterns_outside_bracket.append(word[i]+word[i+1]+word[i+2])
        if is_in_brackets == 1:
            is_in_brackets = 0
        else:
            is_in_brackets = 1
    # compares all the patterns from inside and outside brackets
    for pat1 in patterns_inside_bracket:
        for pat2 in patterns_outside_bracket:
            if pat1[0] == pat2[1] and pat1[1] == pat2[0]:
                return True
    return False

ips = [line for line in sys.stdin]
valid_ip = 0
for ip in ips:
    # convert all the brackets to spaces
    ip = re.sub(r'[\[\]]', ' ', ip)
    if support_ssl(ip):
        valid_ip += 1 

print(valid_ip)