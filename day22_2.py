#!/usr/bin/env python3
import sys
NUM_Y = 26
NUM_X = 38
maze = [[0 for i in range(NUM_X)] for j in range(NUM_Y)]
zero = [0, 0]
goal = [0, NUM_X-1]
for line in sys.stdin:
    if not line.startswith('/dev'):
        continue
    info = line.split()
    [coord, x, y] = info[0].split('-')
    x = int(x[1:])
    y = int(y[1:])
    used = int(info[2][:len(info[2])-1])
    if y == 0 and x == NUM_X-1:
        maze[y][x] = 'G' 
    elif used > 100:
        maze[y][x] = '#'
    elif used == 0:
        zero = [y, x]
        maze[y][x] = 'o'
    else:
        maze[y][x] = '.'
step = 0
while maze[0][0] != 'G':
    [y, x] = zero
    # if not in first row then move zero to the left
    if y > goal[0]+1 and x != 0:
        maze[y][x] = maze[y][x-1]
        maze[y][x-1] = 'o'
        zero = [y, x-1]
    # if in the second row then move left until left of goal
    if y == goal[0]+1 and x >= goal[1]:
        maze[y][x] = maze[y][x-1]
        maze[y][x-1] = 'o'
        zero = [y, x-1]
    # if zero is below G and left move upward
    elif x == goal[1]-1 and y > goal[0]:
        maze[y][x] = maze[y-1][x]
        maze[y-1][x] = 'o'
        zero = [y-1, x]
    # if x is zero then move upward
    elif x == 0 and y != 0:
        maze[y][x] = maze[y-1][x]
        maze[y-1][x] = 'o'
        zero = [y-1, x]
    # if in the first row then move to the right
    elif y == 0 and x != goal[1]+1:
        maze[y][x] = maze[y][x+1]
        maze[y][x+1] = 'o'
        zero = [y, x+1]
    elif y == 0 and x == goal[1]+1:
        maze[y][x] = maze[y+1][x]
        maze[y+1][x] = 'o'
        zero = [y+1, x]
    if maze[y][x] == 'G':
        goal = [y, x]
    step += 1
print(step)