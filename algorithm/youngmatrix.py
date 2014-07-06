### youngmatrix.py
### chenms
### 2013-11-07

def mexists(ymatrix, target):
	row = 0
	col = len(ymatrix[0]) - 1
	max_row = len(ymatrix) - 1
	while row <= max_row and col >= 0:
		if target == ymatrix[row][col]:
			return True
		elif target < ymatrix[row][col]:
			col -= 1
		else:
			row += 1
	return False
## main
ymatrix = [[-1, 3, 6 , 10], [2, 5, 9, 12], [4, 6, 10, 15], [7, 7, 11, 16]]
print ymatrix
target = [-2, 3, 6, 11]
for i in target:
	print i, mexists(ymatrix, i)
	

