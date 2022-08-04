n, m = map(int, input().split())

a = []
for i in range(m):
    package, one = map(int, input().split())
    onePac = one * n

    a.append((min(package, onePac), one))
a.sort()
packCount = n // 6
remain = n % 6

ans = 0
minA = a[0][0]
if packCount != 0:
    ans += minA * packCount
a.sort(key=lambda x:(x[1]))
ans += min(a[0][1]*remain, minA)

subAns = 9999999999
for i in range(len(a)):
    subAns = min(subAns, a[i][1] * n)

ans = min(ans, subAns)
print(ans)