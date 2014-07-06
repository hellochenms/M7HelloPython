#!/usr/bin/python
# -*- coding: utf-8 -*-
# _m7_calc_bmi.py
# chenms
# 2014-07-06

h = float(raw_input('plz input your height(eg. 1.75)...'))
w = float(raw_input('plz input your weight(eg. 65)...'))

bmi = w / (h ** 2)

lowbounds = 18.5
highbounds = 23.9

msg = 'you are healthy.'
if bmi < lowbounds:
	msg = 'you are light.'
elif bmi > 23.9:
	msg = 'you are heavy.'

print 'your bmi is %.2f, the healthy range is %.2f~%.2f.\nso %s' \
	%(bmi, lowbounds, highbounds, msg)