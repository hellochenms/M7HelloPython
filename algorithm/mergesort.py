### mergesort.py
### chenms
### 2013-10-29

from testlistbuilder import buildlist 

def mergesort(src):
	imergesort(src, 0, len(src) - 1)

def imergesort(src, low, high):
	count = high - low + 1
	if count <= 1:
		return
	mid = (low + high) / 2
	llow = low
	lhigh = mid
	rlow = mid + 1
	rhigh = high
	imergesort(src, llow, lhigh)
	imergesort(src, rlow, rhigh)
	merge(src, llow, lhigh, rlow, rhigh)	

def merge(src, llow, lhigh, rlow, rhigh):
	
	#import pdb #TODO
	#pdb.set_trace() #TODO

	left = src[llow:lhigh + 1]
	right = src[rlow:rhigh + 1]
	leftcount = len(left)
	rightcount = len(right)
	l = 0
	r = 0
	s = llow
	while l < leftcount and r < rightcount:
		if left[l] <= right[r]:
			src[s] = left[l]
			l += 1
		else:
			src[s] = right[r]
			r += 1 
		s += 1	
	if l < leftcount:
		while s <= rhigh:
			src[s] = left[l]  
 			l += 1
			s += 1
	else:
		while s <= rhigh:
			src[s] = right[r]
			r += 1
			s += 1
	return		

## main 
if __name__ == "__main__":
	array = buildlist(True)
	print "before:", array
	mergesort(array)
	print "after: ", array

