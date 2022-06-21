def rearrange(array):
    n=len(array)
    negative=[]
    positive=[]
    for i in range(n):
        if array[i] <0:
            negative.append(array[i])
        else:
            positive.append(array[i])
    negative.extend(positive)
    return negative

arr= [2, -3 ,-8 ,9, 6 ,4, 10, -9, 5]
print(rearrange(arr))