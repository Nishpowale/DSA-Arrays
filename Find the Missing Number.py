class Solution:
    def MissingNumber(self,array,n):
        sumtotal=n*(n+1)/2
        arraysum=sum(array)
        return round(sumtotal-arraysum)
