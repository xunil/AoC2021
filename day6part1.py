#!/usr/bin/env python3
import os

#fish_list = [3,4,3,1,2]
# with open('day6.txt') as f:
# 	fish_list = list(map(int, f.readline().split(',')))

def generation(fish_list):
	updated_fish_list = []
	new_fish_list = []
	for timer in fish_list:
		if timer == 0:
			new_fish_list.append(8)
			updated_fish_list.append(6)
		else:
			updated_fish_list.append(timer-1)
	return updated_fish_list + new_fish_list

def fgeneration(fish_in, fish_out):
	new_fish_count = 0
	timerstr = fish_in.read(2)
	while timerstr != '':
		timer = int(timerstr[0])
		if timer == 0:
			new_fish_count = new_fish_count + 1
			fish_out.write('6,')
		else:
			fish_out.write('%d,' % (timer-1))
		timerstr = fish_in.read(2)
	fish_out.write(','.join(['8'] * new_fish_count))


for day in range(0, 256):
	print('         \rday %d' % day, end='\r')
	#fish_list = generation(fish_list)
	with open('day6_population.txt') as fish_in, open('day6_temp.txt', 'w') as fish_out:
		fgeneration(fish_in, fish_out)
	os.rename('day6_temp.txt', 'day6_population.txt')

with open('day6_population.txt') as f:
	fish_list = list(map(int, f.readline().split(',')))
print()

print('After 256 days there are %d fish' % (len(fish_list)))
