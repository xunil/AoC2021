#!/usr/bin/env python3

import re

def line_crosses_point(line, x, y):
	if line[X1] == line[X2] == x and y >= min(line[Y1], line[Y2]) and y <= max(line[Y1], line[Y2]):
		#print('X coordinates equal and y %d >= %d, %d <= %d' % (y, min(line[Y1], line[Y2]), y, max(line[Y1], line[Y2])) )
		return True
	if line[Y1] == line[Y2] == y and x >= min(line[X1], line[X2]) and x <= max(line[X1], line[X2]):
		#print('Y coordinates equal and x %d >= %d, %d <= %d' % (x, min(line[X1], line[X2]), x, max(line[X1], line[X2])) )
		return True
	return False

def display_board(board):
	for row in board:
		for col in row:
			if col == 0:
				print('.', end='')
			else:
				print(col, end='')
		print()

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
# Filter out diagonals
coord_sets = [list(map(int, coord)) for coord in coord_sets if coord[X1] == coord[X2] or coord[Y1] == coord[Y2]]

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

for x in range(min_x, max_x+1):
	for y in range(min_y, max_y+1):
		for line in coord_sets:
			if line_crosses_point(line, x, y):
				#print('Line %s crosses point %d,%d' % (line, x, y))
				print('       \r%d,%d' % (x,y), end='\r')
				board[y][x] = board[y][x] + 1


#display_board(board)
score = len([item for sublist in board for item in sublist if item > 1])
print('Score is %d' % score)