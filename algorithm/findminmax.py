###
def swap(array, i, j):
	temp = array[i]
	array[i] = array[j]
	array[j] = temp

def findminmax(array):
	length = len(array)
	if length == 0:
		return []
	if length == 1:
		return array * 2
	# 
	for i in range(0, length - 1, 2):
		if array[i] > array[i + 1]:
			swap(array, i, i + 1)
	#	
	min = array[0]
	max = array[1]
	for i in range(2, length, 2):
		if array[i] < min:
			min = array[i]
	for i in range(3, length, 2):
		if array[i] > max:
			max = array[i]

	return [min, max]
## main
array = [2, -2, 3, 1, 6, 7, -5, 1, 2, 3, 5]
print "array:", array
minmax = findminmax(array)
print "minmax:", minmax
print "min:", minmax[0], ", max:", minmax[1]
