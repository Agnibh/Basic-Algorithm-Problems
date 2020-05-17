def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints)==0:
        return None

    if len(ints)==1:                        # base case when there is only a single element in the interval
        if ints[0]>0:
            return ints[0],ints[0]       # if the element is greater than 0, then send min value as the highest integer value in python as all other values will be less than this
        return ints[0],ints[0]         # if the element is less than 0, then send max value as the lowest integer value in python

    fin_max=0
    fin_min=0

    mid=len(ints)//2

    left_min,left_max=get_min_max(ints[:mid])       # recursively get the max-min value from the two halves of the array
    right_min,right_max=get_min_max(ints[mid:])

    if left_max>right_max:                          # Compare the max-min values from the two halves
        fin_max=left_max
    else:
        fin_max=right_max

    if left_min<right_min:
        fin_min=left_min
    else:
        fin_min=right_min

    return fin_min,fin_max

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print(get_min_max(l))
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

print(get_min_max([0]))
print(get_min_max([-783,89823,84262837,-2398432984,2736218,28137,5987,-203984]))
print(get_min_max([]))
