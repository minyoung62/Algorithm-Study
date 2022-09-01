n, c = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort()
def isPossible(length):

  cnt = 1
  now = a[0]
  for i in range(1, n):
    if now + length <= a[i]:
      cnt += 1
      now = a[i]

  return cnt >= c

lo = 1
hi = 1000000000
ans = 0
while lo <= hi:
  mid = (lo + hi) // 2

  if isPossible(mid):
    lo = mid + 1
    ans = mid

  else:
    hi = mid - 1
print(ans)
