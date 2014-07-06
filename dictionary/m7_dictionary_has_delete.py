#!/usr/bin/python
# -*- coding: utf-8 -*-
# m7_dictionary_has_delete.py
# chenms
# 2014-07-07

myDict = {'key0':'value0', 'key1':'value1'}
print 'before:', myDict
deleteKey = 'key0'
if myDict.has_key(deleteKey):
    myDict.pop(deleteKey)
print 'after:', myDict
