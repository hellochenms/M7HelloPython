#!/usr/bin/python
# -*- coding: utf-8 -*-
# _m7_calc_index2pagerowcol.py
# chenms
# 2014-07-06

index = raw_input('plz input index...')
index = int(index)
row = raw_input('plz input row count...')
row = int(row)
col = raw_input('plz input col count...')
col = int(col)

page_number = (index - 1) / (row * col) + 1
index_in_page = (index - 1) % (row *col) + 1
row_number = (index_in_page - 1) / col + 1
col_number = (index_in_page - 1) % col + 1

print 'PageNo: %d, RowNo: %d, ColNo: %d' %(page_number, row_number, col_number)