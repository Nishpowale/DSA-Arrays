#Also called the DNF Method
#The Dutch National flag method also used to sort os 1s and 2s 
#https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/

def sort012( array):
    left, right, current = 0, len(array) - 1, 0
    while current <= right:
        if array[current] == 0:
            array[current], array[left] = array[left], array[current]
            left += 1
            current += 1
        elif array[current] == 1:
            current += 1
        else:
            array[current], array[right] = array[right], array[current]
            # current += 1
            right -= 1
    print(array)

Arr=[1,2,1,0,0,0,2,1,0]
sort012(Arr)
