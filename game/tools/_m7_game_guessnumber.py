#!/usr/bin/python
# -*- coding: utf-8 -*-
# _m7_game_guessnumber.py
# chenms
# 2014-07-06

import random

number = random.randint(0, 100)

print 'Game: guess number between 0 and 100'

guess = int(raw_input('plz input...'))

while(guess >= 0 and guess <= 100):
	if guess > number:
		print 'too big'
	elif guess < number:
		print 'too small'
	else:
		print 'you guessed it!'
		break
	guess = int(raw_input('plz input...'))

else:
	print 'number is', number
