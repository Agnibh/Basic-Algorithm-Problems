def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number<0:
        return None

    return find_sqrt(0,number,number)

def find_sqrt(start,end,target):

    if end==1:                              # if the number is 1, return 1
        return 1

    if ((end-start)//2)==0:                 # base case when the interval cannot be divided further i.e the interval consists of only 2 elements, return the start point
        return start

    mid=start+((end-start)//2)              # find the mid of the interval

    if mid*mid==target:                     # if the middle number is the square root of the target, then return the middle number
        return mid

    while mid*mid>target:                   # Reduce the interval by half until we find a number whose square is lesser than the target
        end=mid
        mid=start+((end-start)//2)

    return find_sqrt(mid,end,target)        # Put that as the new start point and recursively call the function



print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

print ("Pass" if  (None == sqrt(-10)) else "Fail")
print ("Pass" if  (28097 == sqrt(789456123)) else "Fail")
