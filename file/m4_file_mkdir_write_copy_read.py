#!/usr/bin/python
# -*- coding: utf-8 -*-
# file_mkdir_write_copy_read.py
# chenms
# 2014-07-06

import os
from shutil import copyfile

# 创建目录
dirName = 'file_mkdir_write_copy_read'
if not os.path.exists(dirName):
    os.mkdir(dirName)

txt = '''\
line0
line1
line2\
'''

fileName = 'file.txt'

# 写文件
srcPath = dirName + os.sep + fileName 
f = file(srcPath, 'w')
f.write(txt)
f.close()

# 复制
destPath = dirName + os.sep + 'copy_' + fileName
copyfile(srcPath, destPath)

# 读文件
f = file(destPath, 'r')
txt = f.read()
print 'txt:\n%s' %(txt, )
f.close()

f = file(destPath, 'r')
lines = f.readlines()
print '\nlines:'
for line in lines:
    # 读到的line中有换行符，所以我们print时加上逗号，避免print的自动换行
    print line,
f.close()

