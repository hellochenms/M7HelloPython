### bubblesort.py
### chenms
### 2013-11-07

def swap(array, i, j):
	temp = array[i]
	array[i] = array[j]
	array[j] = temp

def bubblesort(array):
	length = len(array)
	for i in range(length - 1, 0, -1):
		for j in range(0, i):
			if array[j] > array[j + 1]:
				swap(array, j, j + 1) 
		
## main
array = [3, -5, 0, 9, 2, 6, -13, 26, 7, 56, -1, -2, 2, -6]
print "before:", array
bubblesort(array)
print "after :", array
