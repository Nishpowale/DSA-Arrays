def PalinArray(arr):
    count=0
    n = len(arr)
    for i in range (n):
        s=str(arr[i])
        if s == s[::-1] :
            count +=1
        if count == n :
            print(1)
array=[111 ,222 ,333 ,444, 555]
PalinArray(array)
#For a Palindromic string
def isPalindrome(sS):
	#count=0
    if S == str(S[::-1]):
        return 1
    else :
        return 0


