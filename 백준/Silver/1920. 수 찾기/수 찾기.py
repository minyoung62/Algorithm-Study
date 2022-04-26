n = int(input())
A = list(map(int, input().split()))
m = int(input())
M = list(map(int, input().split()))

A.sort()
def binarySearch(l, r, target):

    while l<=r:
        mid = (l+r) // 2

        if A[mid] == target:
            return 1

        if target > A[mid]:
            l = mid + 1
        else:
            r = mid - 1

    return 0

for i in range(m):
    answer = binarySearch(0, n-1, M[i])
    print(answer)