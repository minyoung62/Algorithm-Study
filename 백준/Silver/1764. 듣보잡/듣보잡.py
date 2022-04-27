import sys
si = sys.stdin.readline
n, m = list(map(int, si().split()))

d =  [0] * n
for i in range(n):
    d[i] = si().rstrip("\n")
d = sorted(d)
b = [0] * m
for i in range(m):
    b[i] = si().rstrip("\n")
b = sorted(b)


def binarySearch(target, l, r, b):

    while l <= r:
        mid = (l + r) // 2

        if b[mid] == target:
            return b[mid]

        elif b[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return None
results = []
for i in range(n):
    target = d[i]
    result = binarySearch(target,0, m-1, b)
    if result == None:
        continue
    else:
        results.append(result)

print(len(results))
for i in range(len(results)):
    print(results[i])