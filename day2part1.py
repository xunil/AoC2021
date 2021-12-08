#!/usr/bin/env python3

horiz_pos = 0
depth = 0

f = open('day2.txt')
instructions = [l.strip().split(' ') for l in f.readlines()]

for instruction,units in instructions:
	if instruction == 'forward':
		horiz_pos = horiz_pos + int(units)
	elif instruction == 'down':
		depth = depth + int(units)
	elif instruction == 'up':
		depth = depth - int(units)

print('Final position is %d horizontal at %d depth' % (horiz_pos, depth))
print('Answer should be %d' % (horiz_pos * depth))