
n = int(input())

testCase = []

for i in range(n):
    a, b = map(int, input().split())

    aList = list(map(int, input().split()))
    bList = list(map(int, input().split()))

    testCase.append((aList, bList))


def binarySearch(target, data):

    res = -1
    start = 0
    end = len(data) - 1
    while start <= end:
        
        mid = (start + end) // 2
        
        if data[mid] < target:
            res = mid
            start = mid + 1
        else:
            end = mid - 1

    return res

for a, b in testCase:
    b.sort()
    c = 0
    for target in a:
        c += binarySearch(target, b) + 1

    print(c)
