### find2numbysum.py
### chenms
### 2013-11-08

from quicksort import quicksort

global_init = False	

def find2num(array, sum):
	# init
	global global_init
	if not global_init:
		quicksort(array)
		global_init = True
		print "Init Finish"
	# check
	low = 0
	high = len(array) - 1
	while low < high:
		if array[low] + array[high] < sum:
			low += 1
		elif array[low] + array[high] > sum:
			high -= 1
		else:
			print "find:", array[low], ",", array[high]
			return True		
	return False
	
## main
array = [3, 2, 1, 9, 15, -4, 25, 12, 8, -1, -2, 5, 7, 0, -6, 11, -9, 4, 6]
print "array:", array
while True:
	sum = raw_input("\nplz input sum...")
	if not sum.isdigit():
		break
	sum = (int)(sum)
	exists = find2num(array, sum)
	print "exists:", exists
