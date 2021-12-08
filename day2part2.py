#!/usr/bin/env python3

aim = 0
horiz_pos = 0
depth = 0

f = open('day2.txt')
instructions = [l.strip().split(' ') for l in f.readlines()]

for instruction,units in instructions:
	if instruction == 'up':
		aim = aim - int(units)
	elif instruction == 'down':
		aim = aim + int(units)
	elif instruction == 'forward':
		horiz_pos = horiz_pos + int(units)
		depth = depth + (aim * int(units))

print('Final position is %d horizontal at %d depth' % (horiz_pos, depth))
print('Answer should be %d' % (horiz_pos * depth))