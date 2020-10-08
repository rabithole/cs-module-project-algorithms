'''
Input: a List of integers
Returns: a List of integers
'''
# def product_of_all_other_numbers(arr):
#     result = 1
#     index = 0
#     index2 = 0
#     for x in arr:
#         if index != len(arr) - 1:
#             result = result * arr[index + 1]
#             index += 1
#         else:
#             arr.insert(index2, result)
#             index2 += 1

def product_of_all_other_numbers(arr):
    # create a an empty list where we'll add the producsts
    # of all other numbers
    result = []
    # create a variable which we'll use to multiply
    # all other numbers with and we'll add to the empty list
    product_of_numbers = 1

    # loop the length of the array
    for index1 in range(len(arr)):
        # loop through the length of the array again
        for index2 in range(len(arr)):
            # check if the first index is equal to the second index
            if index1 == index2:
                # if it is, skip this value
                continue
            # before moving on to the next index, multiply non-skipped value
            # product_of_numbers variable
            product_of_numbers *= arr[index2]

        # after each complete pass of a loop
        # append the product_of_numbers variable, which should hold
        # the result of multiplying every other number except the
        # one that matches the index of our first loop
        result.append(product_of_numbers)
        # before making another pass at the loop
        # reset product_of_numbers to 1
        product_of_numbers = 1

    return result

    



if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]
    arr = [1, 7, 3, 4]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
