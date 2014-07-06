### selectsort.py
### chenms
### 2013-11-07

import pdb #TODO

def selectsort(array):
	length = len(array)
	for i in range(length - 1, 0, -1):

		#pdb.set_trace() #TODO

		max = i
		for j in range(0, i):
			if array[j] > array[max]:
				max = j
		temp = array[i]
		array[i] = array[max]
		array[max] = temp

## main
array = [3, 4, -1, 9, 51, -8, 8, 6, 4, 2, 1, -5]
print "before:", array

#pdb.set_trace() #TODO

selectsort(array)
print "after :", array
