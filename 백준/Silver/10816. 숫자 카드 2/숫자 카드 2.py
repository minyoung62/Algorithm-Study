import sys
si = sys.stdin.readline

n = int(si())
nList = sorted(list(map(int, si().split())))

m = int(si())
mList = list(map(int, si().split()))

def upperbinarySearch(target, l, r):
    res = r + 1
    while l <= r:
        mid = (l + r) // 2

        if nList[mid] >= target:
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    return res

def lowwerbinarySearch(target, l , r):
    res = r + 1
    while l <= r:
        mid = (l + r) // 2
        if nList[mid] > target:
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    return res


for i in range(m):
    target = mList[i]
    print(lowwerbinarySearch(target, 0, n-1) - upperbinarySearch(target, 0, n-1), end=' ')
