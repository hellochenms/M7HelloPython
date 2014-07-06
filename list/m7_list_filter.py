#!/usr/bin/python
# -*- coding: utf-8 -*-
# m7_list_filter.py
# chenms
# 2014-07-07

srcList = ['a_0', 'a_1', 'b_0', 'b_1']
print 'srcList:', srcList
destList = [item for item in srcList if item.startswith('a_')]
print 'filter: startswith \'a_\''
print 'destList:', destList
