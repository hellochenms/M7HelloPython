#!/usr/bin/python
# -*- coding: utf-8 -*-
# _m7_url_extra_suburl_url_regex.py
# chenms
# 2014-07-11

# 提取响应报文中可点击的url

import urllib
import re

url = 'https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/AppDesignBasics/AppDesignBasics.html'

urlPathItemArr = url.split('/')
urlFileName = urlPathItemArr[-1]
urlPathItemArr = urlPathItemArr[0:len(urlPathItemArr) - 1]
urlPathItemCount = len(urlPathItemArr)

result = urllib.urlopen(url)
responseString = result.read()

urlFile = file(urlFileName + '.txt', 'w')

p = re.compile(r'<a.*?a>')
arr = p.findall(responseString)
for item in arr:
    pTitle = re.compile(r'>(.+)<')
    pHref = re.compile(r'href.*?[\'"](.*?)[\'"]')
    matchTitle = pTitle.search(item)
    matchHref = pHref.search(item) 
    if matchTitle and matchHref:
        title = matchTitle.group(1)
#        print 'title:', title
        href = matchHref.group(1)
#        print 'href:', href
        if href.startswith('../'):
            pathItemArr = re.findall(r'\.\./', href)
            curUrlPathItemArr = urlPathItemArr[:urlPathItemCount - len(pathItemArr)]
            subHeadUrl = '/'.join(curUrlPathItemArr)
            #print 'subHeadUrl:', subHeadUrl
            subTailUrl = href[len('../') * len(pathItemArr):]
            #print 'subTailUrl:', subTailUrl
            href = '/'.join([subHeadUrl, subTailUrl])
#            print 'new href:', href
        urlFile.write(title + '\n')
        urlFile.write(href + '\n\n')
#    else:
#        print 'not match:', item

urlFile.close()
