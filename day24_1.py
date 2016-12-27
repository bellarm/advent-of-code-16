#!/usr/bin/env python3
import sys
from itertools import permutations

maze = [[i for i in line.rstrip()] for line in sys.stdin]
dist_between = [[-1 for i in range(8)] for j in range(8)]
NUM_X = len(maze[0])
NUM_Y = len(maze)
# first find location of all point
loc = [(-1,-1)]*8
for y in range(NUM_Y):
    for x in range(NUM_X):
        if maze[y][x] >= '0' and maze[y][x] <= '7':
            i = int(maze[y][x])
            loc[i] = (y, x)
# now find distance between 2 pts
for point in loc:
    to_visit = [point, ]
    found = 0
    [cur_y, cur_x] = point
    visited = [[False for i in range(NUM_X)] for j in range(NUM_Y)]
    dist = [[-1 for i in range(NUM_X)] for j in range(NUM_Y)]
    dist[point[0]][point[1]] = 0
    while len(to_visit):
        [y, x] = to_visit[0]
        to_visit.remove(to_visit[0])
        if visited[y][x]:
            continue
        visited[y][x] = True
        if maze[y][x+1] != '#':
            if dist[y][x+1] == -1:
                dist[y][x+1] = dist[y][x]+1
            to_visit.append((y, x+1))
        if maze[y][x-1] != '#':
            if dist[y][x-1] == -1:
                dist[y][x-1] = dist[y][x]+1
            to_visit.append((y, x-1))
        if maze[y+1][x] != '#':
            if dist[y+1][x] == -1:
                dist[y+1][x] = dist[y][x]+1
            to_visit.append((y+1, x))
        if maze[y-1][x] != '#':
            if dist[y-1][x] == -1:
                dist[y-1][x] = dist[y][x]+1
            to_visit.append((y-1, x))
        if maze[y][x] >= '0' and maze[y][x] <= '7':
            if dist_between[int(maze[cur_y][cur_x])][int(maze[y][x])] == -1:
                dist_between[int(maze[cur_y][cur_x])][int(maze[y][x])] = dist[y][x]
                dist_between[int(maze[y][x])][int(maze[cur_y][cur_x])] = dist[y][x]
                found += 1
comb = permutations(range(8))
shortest_dist = 1000
for n in comb:
    if n[0] != 0:
        continue
    cur_dist = 0
    for i in range(len(n)-1):
        cur_dist += dist_between[n[i]][n[i+1]]
    if cur_dist < shortest_dist:
        shortest_dist = cur_dist
print(shortest_dist)