'''
Input: a List of integers
Returns: a List of integers
'''
i = 0
def moving_zeroes(arr, i):
    print(i)
    if arr[i] != 0:
        arr.insert(0, arr[i])
        arr.pop(i + 1)
    if i == len(arr) - 1:
        return arr
    else:
        i += 1
        return moving_zeroes(arr, i) 
            

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr, i)}")