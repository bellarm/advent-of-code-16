#!/usr/bin/env python3

import sys

def show_maze(maze):
    for y in range(50):
        for x in range(50):
            sys.stdout.write(maze[y][x])
        sys.stdout.write("\n")
    
def is_open_space(x, y):
    input = 1358
    num = bin(x*x + 3*x + 2*x*y + y + y*y + input)
    ones = 0
    for c in num:
        if c == '1':
            ones += 1
    if ones % 2 == 1:
        return False
    return True

# create maze
maze = [['0' for i in range(50)] for j in range(50)]
for y in range(50):
    for x in range(50):
        if x == (1) and y == (1):
            maze[y][x] = 'S'
        elif x == (31) and y == (39):
            maze[y][x] = 'F'
        elif is_open_space(x, y):
            maze[y][x] = '.'
        else:
            maze[y][x] = '#'

# find the path
visited = [[False for i in range(50)] for j in range(50)]
pred = [[(0,0) for i in range(50)] for j in range(50)]
to_visit = [(1, 1), ]
while len(to_visit):
    [x, y] = to_visit[0]
    to_visit.remove(to_visit[0])
    if visited[y][x]:
        continue
    visited[y][x] = True
    if x == 31 and y == 39:
        break
    if maze[y][x+1] != '#' and x != 49:
        if pred[y][x+1] == (0,0):
            pred[y][x+1] = (x, y)
        to_visit.append((x+1, y))
    if maze[y][x-1] != '#' and x != 0:
        if pred[y][x-1] == (0,0):
            pred[y][x-1] = (x, y)
        to_visit.append((x-1, y))
    if maze[y+1][x] != '#' and y != 49:
        if pred[y+1][x] == (0,0):
            pred[y+1][x] = (x, y)
        to_visit.append((x, y+1))
    if maze[y-1][x] != '#' and y != 0:
        if pred[y-1][x] == (0,0):
            pred[y-1][x] = (x, y)
        to_visit.append((x, y-1))

count = 1
[x, y] = pred[y][x]
while maze[y][x] != 'S':
    maze[y][x] = 'O'
    [x, y] = pred[y][x]
    count += 1
show_maze(maze)
print(count)