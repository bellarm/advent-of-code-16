#!/usr/bin/python3.5

steps = [tmp for tmp in input().split(', ')]
x = 0
y = 0
dir = 'N'
for step in steps:
    if step[0] == 'R':
        if dir == 'N':
            x += int(step[1:])
            dir = 'E'
        elif dir == 'S':
            x -= int(step[1:])
            dir = 'W'
        elif dir == 'W':
            y += int(step[1:])
            dir = 'N'
        elif dir == 'E':
            y -= int(step[1:])
            dir = 'S'
    elif (step[0] == 'L'):
        if dir == 'N':
            x -= int(step[1:])
            dir = 'W'
        elif dir == 'S':
            x += int(step[1:])
            dir = 'E'
        elif dir == 'W':
            y -= int(step[1:])
            dir = 'S'
        elif dir == 'E':
            y += int(step[1:])
            dir = 'N'
distance = abs(x) + abs(y)
print(distance)
