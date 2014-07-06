###
def findhalf(array):
	import pdb #TODO
	pdb.set_trace() #TODO
	
	winner1 = 0
	score1 = 0
	winner2 = 0
	score2 = 0
	for i in range(0, len(array)):
		cur = array[i]
		if score1 == 0:
			winner1 = cur
			score1 += 1
		elif cur == winner1:
			score1 += 1
		elif score2 == 0:
			winner2 = cur
			score2 += 1
		elif cur == winner2:
			score2 += 1
		else:
			score1 -= 1
			score2 -= 1
	if score1 >= score2:
		return winner1
	else:
		return winner2	

## main
array = [1, 3, 1, 2, 1, 2, 1, 6, 2, 1]
print "array:", array
half = findhalf(array)
print "half:", half

