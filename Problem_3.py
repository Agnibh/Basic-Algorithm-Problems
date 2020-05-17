def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    num1=0
    num2=0
    exp=0
    arr=mergesort(input_list)                   # merge sort the array

    if (len(arr))%2==0:                         # if the number of elements in the array is even
        for i in range(0,len(arr)-1,2):
            num1+=arr[i]*10**exp                # form the smaller of the two numbers by even indexed elements in increasing units
            num2+=arr[i+1]*10**exp              # form the larger of the two elements by odd indexed elements in increasing units
            exp+=1
    else:
        for i in range(0,len(arr)-2,2):         # if thenumber of elements in the array is odd
            num1+=arr[i]*10**exp                # form the smaller of the two numbers by even indexed elements in increasing units
            num2+=arr[i+1]*10**exp              # form the larger of the two elements by odd indexed elements in increasing units
            exp+=1
        num2+=arr[-1]*10**exp                   # add the last element to larger number at the highest unit
    return [num2,num1]

def mergesort(input_list):                      # Merge Sort Algorithm
    if len(input_list)==1:
        return input_list

    mid=len(input_list)//2

    left=mergesort(input_list[:mid])
    right=mergesort(input_list[mid:])

    return merge(left,right)

def merge(left,right):                         # Merging of two arrays according by comparing each element according to element value
    left_index=0
    right_index=0
    merge=list()

    while left_index<len(left) and right_index<len(right):
        if left[left_index]<right[right_index]:
            merge.append(left[left_index])
            left_index+=1
        else:
            merge.append(right[right_index])
            right_index+=1

    merge+=left[left_index:]
    merge+=right[right_index:]

    return merge

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function ([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function ([[9,8,7,6,5,4,3,2,1], [98642,7531]])
test_function ([[9,8,7,6,5,4,3,2,1,0], [97531,86420]])
