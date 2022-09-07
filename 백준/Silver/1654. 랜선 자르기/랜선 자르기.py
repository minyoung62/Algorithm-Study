k, n = map(int, input().split())
a = [int(input()) for _ in range(k)]

import sys
l = 0
r = sys.maxsize

def isPossible(lanLength):
  cnt = 0
  for i in range(k):
    cnt += a[i] // lanLength

  return cnt >= n
ans = 0
while l <= r:
  mid = (l + r) // 2

  if isPossible(mid):
    l = mid + 1
    ans = mid
  else:
    r = mid - 1

print(ans)
