def max(array):
    max=array[0]
    n=len(array)
    for i in range (0,n):
        if array[i]>max:
            max=array[i]
    print(max)

def min(array):
    min=array[0]
    n=len(array)
    for i in range (0,n):
        if array[i]<min:
            min=array[i]
    print(min)
#The Way thatI have solved is through linear search 
array=[9,8,7,6,5,4,3,2,1]
max(array)
min(array)