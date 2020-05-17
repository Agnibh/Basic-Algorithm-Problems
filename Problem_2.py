def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return search(input_list,number,0,len(input_list)-1)

def search(input_list,number,start,end):

    if start==end:                                      # base case when there is only 1 element in the interval to be searched
        if input_list[start]==number:
            return start
        return -1

    mid=start+((end-start)//2)                          # find the midpoint of the interval

    start_num=input_list[start]                         # numbers according to their indexes
    end_num=input_list[end]
    mid_num=input_list[mid]

    if input_list[mid]==number:                         # if the mid element matches the number, return the mid element
        return mid

    if mid_num>=start_num and number>=start_num and number<=mid_num:    # if the number lies in the sorted list from start element to mid element
        return search(input_list,number,start,mid)                      # then recursivey call the function by changing the end index to mid index

    if end_num>=mid_num and number>=mid_num and number<=end_num:        # if the number lies in the sorted list from mid element to end element
        return search(input_list,number,mid,end)                        # then recursivey call the function by changing the start index to mid index

    if start_num>=mid_num and (number>=start_num or number<=mid_num):   # if the number lies in the unsorted list from start element to mid element
        return search(input_list,number,start,mid)                      # then recursivey call the function by changing the end index to mid index

    if end_num<=mid_num and (number<=end_num or number>=mid_num):       # if the number lies in the unsorted list from mid element to end element
        return search(input_list,number,mid,end)                        # then recursivey call the function by changing the start index to mid index

    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
