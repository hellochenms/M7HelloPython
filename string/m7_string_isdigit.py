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

# �����ֻ��'12'ͨ����isdigit��飬��Ϊ�������ַ���������
# ��������������֣�����Ҫ��������
