def Rearrange( a, n):
    # Your code goes here
    neg=[]
    pos=[]
    for i in range(n):
        if a[i]<0:
            neg.append(a[i])
        else:
            pos.append(a[i])
    
    neg.extend(pos)
    for i in range(n):
        a[i]=neg[i]
    return a  
