#!/usr/bin/python
# -*- coding: utf-8 -*-
# m7_string_isdigit.py
# chenms
# 2014-07-06

srcList = ['ab', '12', '-12', '12.3', 'ab12']
print 'srcList', srcList
for item in srcList:
    if item.isdigit():
        print item

# 结果是只有'12'通过了isdigit检查，因为其所有字符都是数字
# 如果想检查所有数字，看来要用正则了
