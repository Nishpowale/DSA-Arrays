def rotate(array):
    n=len(array)
    x=arr[n-1]
    res=[]
    for i in range (n-1,0,-1):
        arr[i] =arr[i-1]
    arr[0]=x
    return arr
arr=[1,2,3,4,5]
print(rotate(arr))