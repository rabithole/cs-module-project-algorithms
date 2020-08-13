'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
list1 = [2,2,3,3,4,4,5,5,6,7,7,8,8]

# def single_number(arr):
# 	for x in arr:
# 		if arr.count(x) == 1:
# 			return x

# print(single_number(list1))

s = set() # O(1)

def single_number(arr):
	for x in arr: # O(n)
		if x in s: # O(1)
			s.remove(x) # O(1)
		else:
			s.add(x) # O(1)

	return list(s)[0] # O(1)

print(single_number(list1))



# if __name__ == '__main__':
#     # Use the main function to test your implementation
#     arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

#     print(f"The odd-number-out is {single_number(arr)}")