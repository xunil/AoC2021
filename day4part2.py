#!/usr/bin/env python3

from itertools import islice
from operator import methodcaller

def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


with open('day4.txt') as f:
	calls = list(map(int, f.readline().split(',')))
	f.readline() # Throw away blank line

	# Good luck debugging this one.  :|
	boards = [[list(map(int, filter(lambda x: len(x)>0, row.strip().split(' ')))) for row in board] for board in list(chunk(filter(lambda x: len(x)>1, f.readlines()), 5))]


def winning_board(calls, board):
	if len(calls) < 5:
		return False # No one can have won with fewer than 5 calls
	for row in board:
		if len(set(row) & set(calls)) == 5:
			return True
	for i in range(0, 5):
		if len(set(map(lambda x: x[i], board)) & set(calls)) == 5:
			return True
	return False

def score_board(calls, board):
	return sum(set([item for sublist in board for item in sublist]) - set(calls)) * calls[-1]

for i in range(0, len(calls)+1):
	losers = [board for board in boards if not winning_board(calls[:i], board)]
	if len(losers) == 1:
		print('We have the biggest loser: %s' % losers)
		while(not winning_board(calls[:i], losers[0])):
			i = i + 1
		score = score_board(calls[:i], losers[0])
		print('Score is %d' % score)
		break

