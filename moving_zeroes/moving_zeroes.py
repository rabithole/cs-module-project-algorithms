'''
Input: a List of integers
Returns: a List of integers
'''
# i = 0
newArr = []

def moving_zeroes(arr):
	# Loop through array
	# If int is > 0, insert() at zero
	for x in arr:
		if x > 0: 
			newArr.insert(0, x)
		if x <= 0:
			newArr.append(x)
			continue
	return newArr
# if __name__ == '__main__':
#     # Use the main function here to test out your implementation
#     arr = [0, 3, 1, 0, -2]

    # print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
print('')
testList = [100, 0, -3, -20, 0, 30, 10, 3]

print(moving_zeroes(testList))
print('')