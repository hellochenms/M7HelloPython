###

def findmorehalf(array):
	winner = 0
	score = 0
	for i in range(0, len(array)):
		cur = array[i]
		if score == 0:
			winner = cur
			score += 1
		elif winner == cur:
			score += 1
		else:
			score -= 1
	return winner

## main
array = [1, 3, 2, 4, 2, 2, 1, 2, 1]
print "array:", array
morehalf = findmorehalf(array)
print "morehalf:", morehalf
