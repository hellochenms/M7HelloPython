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
# ����dict����¼�Ѿ���destListĳ�㼶��item
destDict = {}
# ����list����¼�����ε�������srcList��ɾ��item
deleteList = []

# ����������ֱ��������ֹ����
isEnd = False
lastSrcListLength = len(srcList)
while (isEnd == False):
    # һ�ε���
    deleteList = []
    for item in srcList:    
        # ���item��PIDΪ0������PID��Ӧ��item�Ѿ���destDic�У���item����destList�ĺ���λ��
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
