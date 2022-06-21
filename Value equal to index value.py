
def valueEqualToIndex(arr):
    ans = []
    n=len(arr)
    for i in range(n):
        if arr[i] == i + 1:
            ans.append(arr[i])

    print(ans)
arr=[625 ,538 ,549, 484 ,596, 42, 603,351,292,10]
arr2=[1,2,3,4,5,6,7]
valueEqualToIndex((arr))
valueEqualToIndex((arr2))