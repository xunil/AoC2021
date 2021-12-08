#!/usr/bin/env python3

with open('day3.txt') as f:
	readings = [int(b.strip(), 2) for b in f.readlines()]
bit_depth = 12
# bit_depth = 5
# readings = [
# 	0b00100,
# 	0b11110,
# 	0b10110,
# 	0b10111,
# 	0b10101,
# 	0b01111,
# 	0b00111,
# 	0b11100,
# 	0b10000,
# 	0b11001,
# 	0b00010,
# 	0b01010
# ]

def most_common(rs, bit):
	counts = [0, 0]

	for reading in rs:
		idx = (1 if reading & 2**bit == 2**bit else 0)
		counts[idx] = counts[idx] + 1

	if counts[0] == counts[1] or counts[1] > counts[0]:
		return 1
	else:
		return 0

def least_common(rs, bit):
	return 1 & ~most_common(rs, bit)

def bit_match(r, bit, val):
	return ((r & 2**bit) >> bit) == val

def filter_readings(rs, bit, comp_func):
	return [r for r in rs if bit_match(r, bit, comp_func(rs, bit))]

def doit(rs, bit, comp_func):
	if len(rs) == 1:
		return rs[0]
	if len(rs) == 0:
		raise ValueError('List of values is empty')
	return doit(filter_readings(rs, bit, comp_func), bit-1, comp_func)

oxygen_reading = doit(readings, bit_depth-1, most_common)
co2_scrubber_reading = doit(readings, bit_depth-1, least_common)

print("Oxygen reading: %d  CO2 scrubber reading: %d  Life support rating: %d" % (oxygen_reading, co2_scrubber_reading, oxygen_reading * co2_scrubber_reading))
