#This is a program to count the number of consecutive ones occuring in an array
#Given binary array, find count of maximum number of consecutive 1’s present in the array.
#efficient solution is traverse array from left to right. If we see a 1, we increment count
#and compare it with maximum so far. If we see a 0, we reset count as 0

def getMaxLength(array):
    n = len(array)
    count=0
    maximum=0
    for i in range(n):
        if array[i] == 1 :
            count +=1
        else :
            count =0
    maximum=count

    print(maximum)

arr = [1, 1, 0, 0, 1, 0, 1,0, 1, 1, 1, 1]
arr2=[1,0,1,1,0,1]
#n=len(arr)
getMaxLength(arr)
getMaxLength(arr2)

