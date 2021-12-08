import sys
import os

f = open('day1.txt')
readings = [int(l.strip()) for l in f.readlines()]
f.close()

last_value = readings[0]
increases = 0

for reading in readings:
	if reading > last_value:
		increases = increases + 1
	last_value = reading

print('Number of increases in readings: %d\n' % increases)
