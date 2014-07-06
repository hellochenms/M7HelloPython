### testlistbuilder.py
### chenms
### 2013-11-09

import random

def buildlist(allow_negative = False, count = 20):
	lfrom = 0
	lto = 99
	if allow_negative:
		lfrom = -49
		lto = 49
	resultlist = []
	for i in range(0, count):
		resultlist.append(random.randint(lfrom, lto))
	return resultlist

## main
if __name__ == "__main__":
	resultlist = buildlist()
	print resultlist
