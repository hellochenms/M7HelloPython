#!/usr/bin/python
# -*- coding: utf-8 -*-
# main.py
# chenms
# 2014-07-07

# 本模块被import引用时，方法__main__中的测试代码不会被调用，
# 直接执行本文件时才会被执行，
# 没写在__main__中的代码，被import时就直接执行了，
# 一般写了模块后，可以在模块中实现main作为demo。

print 'print when be import'

# main
if __name__ == '__main__': 
    print 'main'
