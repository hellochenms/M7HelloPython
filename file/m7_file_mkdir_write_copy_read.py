#!/usr/bin/python
# -*- coding: utf-8 -*-
# file_mkdir_write_copy_read.py
# chenms
# 2014-07-06

import os
from shutil import copyfile

# ����Ŀ¼
dirName = 'file_mkdir_write_copy_read'
if not os.path.exists(dirName):
    os.mkdir(dirName)

txt = '''\
line0
line1
line2\
'''

fileName = 'file.txt'

# д�ļ�
srcPath = dirName + os.sep + fileName 
f = file(srcPath, 'w')
f.write(txt)
f.close()

# ����
destPath = dirName + os.sep + 'copy_' + fileName
copyfile(srcPath, destPath)

# ���ļ�
f = file(destPath, 'r')
txt = f.read()
print 'txt:\n%s' %(txt, )
f.close()

f = file(destPath, 'r')
lines = f.readlines()
print '\nlines:'
for line in lines:
    # ������line���л��з�����������printʱ���϶��ţ�����print���Զ�����
    print line,
f.close()

