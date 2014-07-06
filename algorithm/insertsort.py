### insertsort.py
### chenms
### 2013-11-07

def insertsort(array):
	length = len(array)
	for i in range(1, length):
		pos = i
		temp = array[i]
		for j in range(i - 1 , -1, -1):
			if array[j] > temp:
				array[j + 1] = array[j]
				pos -= 1
		array[pos] = temp						

## main
array = [3, 15, -2, 6, 1, 7, -13, 6, 43, 0, -7]
print "before:", array

#import pdb #TODO
#pdb.set_trace() #TODO 

insertsort(array)
print "after :", array
