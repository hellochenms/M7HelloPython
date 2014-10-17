#!/usr/bin/python
# -*- coding: utf-8 -*-
# _tools_file_wark_rename.py
# chenms
# 2014-07-07

# 为指定目录下所有文件添加m7_前缀
# （.git下文件、.DS_Store文件以及本来就以m7_开头的文件除外）

import os

rootDir = ''
for path, subdir, files in os.walk(rootDir):
    if path == '.' or path.find('git') != -1 or path.find('DS_Store') != -1:
        continue
    for filename in files:
        if not filename.startswith('m7_') and not filename.startswith('.'):
            os.rename(os.path.join(path, filename), os.path.join(path, 'm7_' + filename))
