### binarysearch.py
### chenms
### 2013-11-08

def binarysearch(array, num, low = 0, high = -1):
	
	#import pdb #TODO
	#pdb.set_trace()
	if high == -1:
		high = len(array) - 1
	while low <= high:
		mid = (low + high) / 2
		item = array[mid]
		if num < item:
			high = mid - 1
		elif num > item:
			low = mid + 1 		
		else:
			return mid
	return -1

## main
#sortedarray = [-44, - 32, -22, -19, -18, -15, -15, -9, -8, -5, -2, 0, 1, 3, 4, 5, 5, 7, 12, 15, 19, 22, 26, 37, 49] 
#print "array:", sortedarray
#while True:
#	num = raw_input("\nplz input num... ")
#	if num.startswith("-"):
#		absnum = num[1:]
#	else:
#		absnum = num
#	if not absnum.isdigit():
#		break
#	num = int(num)
#	pos = binarysearch(sortedarray, num)
#	print "position:", pos
