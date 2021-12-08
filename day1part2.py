#!/usr/bin/env python3
import sys
import os

f = open('day1.txt')
readings = [int(l.strip()) for l in f.readlines()]
f.close()

def window_sum(r, i):
	return r[i] + r[i+1] + r[i+2]

last_window = window_sum(readings, 0)
increases = 0

for index, reading in enumerate(readings):
	if len(readings) < index+4:
		break
	this_window = window_sum(readings, index+1)
	print('This window: %d  Last window: %d' % (this_window, last_window))
	if this_window > last_window:
		increases = increases + 1
		print('*** Increase! (now %d)' % increases)
	last_window = this_window

print('Number of increases in readings: %d' % increases)
