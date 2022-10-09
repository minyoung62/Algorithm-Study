
n, k = tuple(map(int, input().split()))
a = list(map(int, input().split()))

d = dict()

r = -1
ans = 0
cnt = 0
for l in range(n):
  while r + 1 < n and d.get(a[r+1], 0) + 1 <= k:
    r += 1
    d[a[r]] = d.get(a[r], 0) + 1

  ans = max(ans, r - l + 1)

  if d[a[l]] != 0:
    d[a[l]] -= 1

print(ans)
