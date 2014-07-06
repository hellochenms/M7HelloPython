### leftrotate.py
### chenms
### 2013-10-24

K = 30000

def mleftrotate(array, k):
	last_index = len(array) - 1
	mreverse(array, 0, k - 1)
	mreverse(array, k, last_index)
	mreverse(array, 0, last_index)	
	
def mreverse(array, low, high):
	print "mreverse"
	loop_count = (high - low + 1) / 2
	sum = low + high
	for i in range(low, low + loop_count):
		temp = array[i]
		array[i] = array[sum - i]
		array[sum - i] = temp

## main
array = list("helloworld")
print "before:", array
K = K % len(array)
mleftrotate(array, K)
print "after:", array


