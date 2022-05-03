t = int(input())
tList = [
    [] 
    for _ in range(t)
]
for i in range(t):
    a, b = tuple(map(int, input().split()))
    aList = list(map(int, input().split()))
    bList = list(map(int, input().split()))

    tList[i].append(aList)
    tList[i].append(bList)

def BS(l, r, arr, target):
    res = -1
    while l <= r:
        mid = (l + r) // 2

        if arr[mid] < target:
            res = mid
            l = mid + 1
        else:
            r = mid - 1
    return res


for i in range(t):
    aList, bList = tList[i][0], tList[i][1]
    answer = 0    
    bList.sort()
    n = len(bList)
    for i in aList:
        answer += BS(0, n-1, bList, i) + 1
    print(answer)