'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
output = [] 
def sliding_window_max(nums, k):
    # print(len(nums) - 1)
    a = k - k
    win = nums[a:k]
    endOfNums = nums[len(nums) - 1]
    # print(endOfNums)
    endOfwin = win[len(win) - 1]
    # print(endOfwin)

    if endOfNums == len(win) - 1:
        # print('end of nums', output) 
        return output
    else:
        output.append(max(win))
        # print(output)
        a += 1
        k += 1
        # print(a, k)
    return sliding_window_max(nums, k)
    

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
