### heapsort.py
### chenms
### 2013-11-07

GLOBAL_COUNT = 0 #TODO

def swap(array, i, j):
	temp = array[i]
	array[i] = array[j]
	array[j] = temp

def heap_adjust(array, pos, length):
	if length <= 1:
		return
	j = pos * 2 + 1
	while(j < length):
		global GLOBAL_COUNT #TODO
		GLOBAL_COUNT += 1 #TODO
		if (j + 1 < length and array[j] < array[j + 1]):
			j += 1
		if (array[pos] >= array[j]):
			break
		swap(array, pos, j)
		pos = j
		j = pos * 2 + 1

def heapsort(array):
	length = len(array)

	# build heap	
	for i in range((length - 1 - 1) / 2, -1, -1):
		heap_adjust(array, i,  length)	
	print "heap:  ", array

	# sort
	for i in range(length - 1, 0, -1):
		swap(array, 0, i)
		heap_adjust(array, 0, i)

## main
array = [-1, 3, -4, 7, 4, 11, 6, 21, 3, -23, 12, 11, 2]
print "before:", array
heapsort(array)
print "after: ", array
print "count: ", GLOBAL_COUNT
