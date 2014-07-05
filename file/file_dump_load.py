#!/usr/bin/python
# -*- coding: utf-8 -*-
# file_dump_load.py
# chenms
# 2014-07-06

import cPickle as p

list = [0, '1', {'key0':'value0', 'key1':'value1'}, ('0', 1)]
path = 'file_dump_load'

# ±£¥Ê
f = file(path, 'w')
p.dump(list, f)
f.close()
    
# ‘ÿ»Î
f = file(path, 'r')
list = p.load(f)
print list
f.close()
