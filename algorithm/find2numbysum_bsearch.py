### find2numbysum_bsearch.py
### chenms
### 2013-11-08

from quicksort import quicksort
from binarysearch import binarysearch

global_init = False	

def find2num(array, sum):
	global global_init
	if not global_init:
		quicksort(array)
		global_init = True
		print "Init Finish"
		print "sort:", array
	length = len(array)
	pos = -1
	for i in range(0, length - 1):
		pos = binarysearch(array, sum - array[i], i + 1, length - 1)
		if pos >= 0:
			print array[i], ",", array[pos]
			return True
	return False
	
## main
array = [3, 2, 1, 9, 15, -4, 25, 12, 8, -1, -2, 5, 7, 0, -6, 11, -9, 4, 6]
print "array:", array
while True:
	sum = raw_input("\nplz input sum...")
	abssum = sum
	if sum.startswith("-"):
		abssum = sum[1:]
	if not abssum.isdigit():
		break
	sum = int(sum)
	exists = find2num(array, sum)
	print "exists:", exists
