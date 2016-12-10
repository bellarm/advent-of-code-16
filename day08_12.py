#!/usr/bin/python3.5

import sys, re

def show(screen):
    for y in range(6):
        for x in range(50):
            sys.stdout.write(screen[y][x])
        sys.stdout.write("\n")
    sys.stdout.write("\n")

def count_pixel(screen):
    on = 0
    for y in range(6):
        for x in range(50):
            if screen[y][x] == '#':
                on += 1
    return on

def turn_on(screen, col, row):
    for y in range(row):
        for x in range(col):
            screen[y][x] = '#'
    
def rotate_col(screen, col, pixel):
    copy = [screen[i][col] for i in range(6)]
    for y in range(6):
        screen[(y+pixel)%6][col] = copy[y]
    
def rotate_row(screen, row, pixel):
    copy = [screen[row][i] for i in range(50)]
    for x in range(50):
        screen[row][(x+pixel)%50] = copy[x]
    
screen = [['.' for x in range(50)] for y in range(6)]
instructions = [line for line in sys.stdin]
for instr in instructions:
    if re.match(r'^rect', instr):
        size = instr.split(' ')[1].split('x')
        turn_on(screen, int(size[0]), int(size[1]))
    if re.match(r'rotate row', instr):
        pixel = int(instr.split(' ')[4])
        row = int(instr.split(' ')[2].split('=')[1])
        rotate_row(screen, row, pixel)
    if re.match(r'rotate col', instr):
        pixel = int(instr.split(' ')[4])
        col = int(instr.split(' ')[2].split('=')[1])
        rotate_col(screen, col, pixel)
show(screen)
print(count_pixel(screen))