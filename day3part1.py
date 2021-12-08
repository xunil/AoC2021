#!/usr/bin/env python3

f = open('day3.txt')

readings = [int(b.strip(), 2) for b in f.readlines()]

counts = [0, 0]
gamma = 0
epsilon = 0

for i in range(0, 12):
	for reading in readings:
		idx = (1 if reading & 2**i == 2**i else 0)
		counts[idx] = counts[idx] + 1
	if counts[1] > counts[0]:
		gamma = gamma | 1<<i
	counts = [0, 0]

epsilon = ((2**12) - 1) - gamma

print("Gamma is %d (%s), epsilon is %d (%s)" % (gamma, bin(gamma), epsilon, bin(epsilon)))
print("Power consumption is %d" % (gamma*epsilon))