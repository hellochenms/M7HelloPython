### maxk.py
### chenms
### 2013-10-29

#import pdb #TODO

K = (int)(raw_input("plz input K..."))

def partition(array, low, high):
	llow = low - 1
	pivot = array[high]
	for check in range(low, high):
		if array[check] < pivot:
			llow += 1
			temp = array[llow]
			array[llow] = array[check]
			array[check] = temp
		check += 1
	temp = array[llow + 1]
	array[llow + 1] = array[high]
	array[high] = temp
	return llow + 1
			
def maxk(array, k, result, low, high):

	#pdb.set_trace() #TODO
	
	if k <= 0:
		return
	if high - low + 1 == k:
		result.extend(array[low:high + 1])
		return
	mid = partition(array, low, high);
	
	#pdb.set_trace() #TODO
	
	#print "mid:", mid, "; array[low:high + 1]:",array[low:high + 1]
	mk = high - mid
	if mk == k:
		result.extend(array[mid + 1:high + 1])
	elif mk + 1 == k:
		result.extend(array[mid:high + 1])
	elif mk > k:
		maxk(array, k, result, mid + 1, high)
	elif mk + 1 < k:
		result.extend(array[mid:high + 1])
		maxk(array, k -mk - 1, result, low, mid - 1)

## main
array = [3, 1, -3, 6, 7, -5, 2, 11]
print "array:", array
if K > len(array):
	K = len(array)
elif K < 0:
	K = 0
maxkarray = []
maxk(array, K, maxkarray, 0, len(array) - 1)
print "maxk:", maxkarray

