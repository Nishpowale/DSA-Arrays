
class Solution:
    def minValue(self, a, b, n):
        # Your code goes here
        a.sort()
        b.sort(reverse = True)
        n=0
        list=[]
        for i in range(len(a)):
            prod=a[n]*b[n]
            n+=1
            list.append(prod)
        return sum(list)
        


#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.minValue(a, b, n))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
