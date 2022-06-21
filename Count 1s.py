#This is a program to count the number of consecutive ones occuring in an array
#Given binary array, find count of maximum number of consecutive 1’s present in the array.
#efficient solution is traverse array from left to right. If we see a 1, we increment count
#and compare it with maximum so far. If we see a 0, we reset count as 0

def getMaxLength(arr, n):
    # initialize count
    count = 0

    # initialize max
    result = 0

    for i in range(0, n):

        # Reset count when 0 is found
        if (arr[i] == 0):
            count = 0

        # If 1 is found, increment count
        # and update result if count
        # becomes more.
        else:

            # increase count
            count += 1
            result = max(result, count)

    return result
arr2=[1,0,1,1,0,1]
n=len(arr2)
#getMaxLength(arr)
print(getMaxLength(arr2,n))

