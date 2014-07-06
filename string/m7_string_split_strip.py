#!/usr/bin/python
# -*- coding: utf-8 -*-
# m7_string_split_strip.py
# chenms
# 2014-07-07

txt = 'a,b, c\n,    d    ,    e'
print 'txt:', txt
srcList = txt.split(',')
print 'srcList:', srcList
destList = [item.strip() for item in srcList]
print 'destList:',destList

