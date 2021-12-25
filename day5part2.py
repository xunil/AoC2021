#!/usr/bin/env python3

import re

def display_board(board):
	for row in board:
		for col in row:
			if col == 0:
				print('.', end='')
			else:
				print(col, end='')
		print()

def direction(c1, c2):
	if c2 > c1:
		return 1
	elif c2 < c1:
		return -1
	return 0


X1 = 0
Y1 = 1
X2 = 2
Y2 = 3

# input_lines = [
# '0,9 -> 5,9\n',
# '8,0 -> 0,8\n',
# '9,4 -> 3,4\n',
# '2,2 -> 2,1\n',
# '7,0 -> 7,4\n',
# '6,4 -> 2,0\n',
# '0,9 -> 2,9\n',
# '3,4 -> 1,4\n',
# '0,0 -> 8,8\n',
# '5,5 -> 8,2\n'
# ]

with open('day5.txt') as f:
	input_lines = f.readlines()

coord_sets = [re.match(r'(\d+),(\d+) -> (\d+),(\d+)', line).groups() for line in input_lines]
coord_sets = [list(map(int, coord)) for coord in coord_sets]
# Determine size of the board from min and max values of coordinate sets
min_x = 2**32
min_y = 2**32
max_x = -2**32
max_y = -2**32
for coord in coord_sets:
	if min_x > min(coord[X1], coord[X2]):
		min_x = min(coord[X1], coord[X2])
	if min_y > min(coord[Y1], coord[Y2]):
		min_y = min(coord[Y1], coord[Y2])
	if max_x < max(coord[X1], coord[X2]):
		max_x = max(coord[X1], coord[X2])
	if max_y < max(coord[Y1], coord[Y2]):
		max_y = max(coord[Y1], coord[Y2])

print('Board ranges from %d,%d to %d,%d' % (min_x,min_y,max_x,max_y))

board = [[0 for y in range(0, max_y+2)] for x in range(0, max_x+2)]

for line in coord_sets:
	print('%d,%d,%d,%d' % tuple(line))

	xdist = abs(line[X1] - line[X2])
	ydist = abs(line[Y1] - line[Y2])

	xdir = direction(line[X1], line[X2])
	ydir = direction(line[Y1], line[Y2])
	x = line[X1]
	y = line[Y1]
	while (x,y) != (line[X2]+(1*xdir),line[Y2]+(1*ydir)):
		print('         \r   %d,%d' % (x,y), end='\r')
		board[y][x] = board[y][x] + 1
		x = x + (1*xdir)
		y = y + (1*ydir)
	print()


#display_board(board)
score = len([item for sublist in board for item in sublist if item > 1])
print('Score is %d' % score)