import sys
si = sys.stdin.readline

n = int(si())
arr = list(map(int, si().split()))
arr.sort()
x = int(si())


def binarySearch(target, l, r):

    while l <= r:
        mid = (l + r) // 2
        
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    
    return None
count = []
for i in range(n):
    ai = arr[i]
    if ai < x:
        target = x - ai
        result = binarySearch(target, 0, n-1)
        if result != None:
            count.append((ai, result))
print(len(count)//2)