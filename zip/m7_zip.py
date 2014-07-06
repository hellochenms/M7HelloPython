#!/usr/bin/python
# -*- coding: utf-8 -*-
# m7_zip.py
# chenms
# 2014-07-06

import os
import zipfile

rootDir = 'dir'
destFileName = 'dest.zip'
zip = zipfile.ZipFile(destFileName, 'w', zipfile.ZIP_DEFLATED)
for path, subdir, files in os.walk(rootDir):
    for fileName in files:
	    zip.write(os.path.join(path, fileName))
zip.close
