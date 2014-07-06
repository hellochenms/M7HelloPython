#!/usr/bin/python
# -*- coding: utf-8 -*-
# _m7_calc_seconds2hms.py
# chenms
# 2014-07-06

seconds = raw_input('plz input seconds...')

seconds = int(seconds)
h = seconds / 3600
m = seconds % 3600 / 60
s = seconds % 3600 % 60

print '%02d:%02d:%02d' % (h, m, s)