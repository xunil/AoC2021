#!/usr/bin/env python3

def generation(population):
	time_0_fish = population.pop(0)
	population.append(time_0_fish)
	population[6] = population[6] + time_0_fish
	return population

#fish_list = [3,4,3,1,2]
with open('day6.txt') as f:
	fish_list = list(map(int, f.readline().split(',')))

population = [0] * 9

for fish in fish_list:
	population[fish] = population[fish] + 1

for day in range(0, 256):
	population = generation(population)

print('Count of fish after 256 days: %d' % sum(population))