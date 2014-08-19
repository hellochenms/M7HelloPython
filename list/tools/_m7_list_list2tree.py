#!/usr/bin/python
# -*- coding:utf-8 -*- 

### list2tree.py
### chenms
### 2014-8-19

import json

srcJsonPath = './_m7_list_list2tree.txt'
srcJsonString = file(srcJsonPath, 'r').read()
srcList = json.loads(srcJsonString)
destList = []
# 辅助dict，记录已经在destList某层级的item
destDict = {}
# 辅助list，记录将本次迭代将从srcList中删除item
deleteList = []

# 反复迭代，直到符合终止条件
isEnd = False
lastSrcListLength = len(srcList)
while (isEnd == False):
    # 一次迭代
    deleteList = []
    for item in srcList:    
        # 如果item的PID为0，或其PID对应的item已经在destDic中，则将item置入destList的合适位置
        if item['PID'] == 0:
            item['sublist'] = []
            destList.append(item)
            destDict[item['ID']] = item
            deleteList.append(item)    
        elif destDict.has_key(item['PID']):
            item['sublist'] = []
            pItem = destDict.get(item['PID'])
            pItem['sublist'].append(item)
            destDict[item['ID']] = item
            deleteList.append(item)
    for deleteItem in deleteList:
        srcList.remove(deleteItem)
    if len(srcList) == 0 or lastSrcListLength == len(srcList):
        isEnd = True
    lastSrcListLength = len(srcList)

destJsonString = json.dumps(destList)
print destJsonString
