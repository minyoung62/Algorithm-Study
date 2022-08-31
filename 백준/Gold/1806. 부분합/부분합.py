n, s = map(int, input().split())

a = list(map(int, input().split()))

import sys
R = -1
ans = sys.maxsize
cnt = 0
for L in range(n):
  while R + 1 < n and cnt < s:
    R += 1
    cnt += a[R]

  if cnt >= s:
    ans = min(ans, R - L + 1)

  cnt -= a[L]

if ans == sys.maxsize:
  ans = 0
print(ans)
