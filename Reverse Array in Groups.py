def reverseInGroups(arr, N, k):
    i = 0
    while i < N:
        left = i
        right = min(i + k - 1, N - 1)
        # N-1 is done when the k is not a multiple of n anymore
        # which means that not enought elements present in the
        # remainign array
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        i += k
    return arr


arr = [1, 2, 3, 4, 5, 6,
       7, 8]

k = 3
N = len(arr)
reverseInGroups(arr, N, k)