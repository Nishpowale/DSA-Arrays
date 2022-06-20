def revlist(Arr, start , end):
    while start < end :
        Arr[start], Arr[end] = Arr[end], Arr[start]
        start +=1
        end -= 1
Arr= [1,2,3,4,5,6,7,8]
print(Arr)
revlist(Arr,0,3)
print(Arr)
