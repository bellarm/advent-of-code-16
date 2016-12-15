#!/usr/bin/python3.5

import sys, re
text = input()

# start and end are pos of the brackets
def expand(start, end):
    global text
    [num_char, num_time] = text[start+1:end-1].split('x')
    num_char = int(num_char)
    num_time = int(num_time)
    string_start = end
    string_end = string_start+num_char
    new_string = text[string_start:string_end]*num_time
    text = text.replace(text[start:string_end], new_string, 1)
    return start

i = 0
while i < len(text):
    if text[i] == '(':
        end = i
        while(text[end] != ')'):
            end += 1
        end += 1
        i = expand(i, end)
    else:
    	i += 1
    print(i)
print(len(text))