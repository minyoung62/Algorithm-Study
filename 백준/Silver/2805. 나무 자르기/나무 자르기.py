import sys
si = sys.stdin.readline

n, m = tuple(map(int, si().split()))

nList = list(map(int, si().split()))


l, r , ans = 0, 2000000000, 0

def determination(mid):
    sum = 0
    for i in range(n):
        if nList[i] > mid:
            sum += nList[i] - mid
    
    return sum >= m

def binarySearch(l, r, ans):

    while l <= r:
        mid = (l + r ) // 2
        
        if determination(mid):
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans
ans = binarySearch(l, r, ans)
print(ans)