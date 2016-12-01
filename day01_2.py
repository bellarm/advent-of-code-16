#!/usr/bin/python3.5

steps = [tmp for tmp in input().split(', ')]
# a bit dodgy...
visited = [[0 for x in range(500)] for y in range(500)]
x = 0
y = 0
prev_y = 0
prev_x = 0
dir = 'N'
for step in steps:
    # print(step)
    prev_x = x
    prev_y = y
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

    if prev_y == y:
        # just mark x
        if x >= prev_x:
            step = 1
        else:
            step = -1
        for i in range(prev_x, x, step):
            # print("(" + str(i) + "," + str(y) + ")")
            if visited[250+i][250+y] == 1:
                distance = abs(i) + abs(y)
                print(distance)
                # break
            visited[250+i][250+y] = 1
    elif prev_x == x:
        if y >= prev_y:
            step = 1
        else:
            step = -1
        for i in range(prev_y, y, step):
            # print("(" + str(x) + "," + str(i) + ")")
            if visited[250+x][250+i] == 1:
                distance = abs(i) + abs(x)
                print(distance)
                # break
            visited[250+x][250+i] = 1
    # else:
        # print("wtf")
