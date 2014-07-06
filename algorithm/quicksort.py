### quicksort.py
### chenms
### 2013-10-22

import random

## quicksort
def partition(tlist, low, high):
	llow = low - 1
	check = low
	while check <= high - 1:
		if tlist[check] < tlist[high]:
			llow += 1
			temp = tlist[llow]
			tlist[llow] = tlist[check]
			tlist[check] = temp
		check += 1
	temp = tlist[llow + 1]
	tlist[llow + 1] = tlist[high]
	tlist[high] = temp
	return llow + 1

def quicksorti(tlist, low, high):
	if low >= high:
		return
	center = partition(tlist, low, high)
	quicksorti(tlist, low, center - 1)
	quicksorti(tlist, center + 1, high)

def quicksort(array):
	quicksorti(array, 0, len(array) - 1)

## main
if __name__ == "__main__":
	tlist = []
	for i in range(0, 20):
		tlist.append(random.randint(1, 100))
	print "before: %s" %(tlist)
	quicksort(tlist);
	print "after: %s" %(tlist)

