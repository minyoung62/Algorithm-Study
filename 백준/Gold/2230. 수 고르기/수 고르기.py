n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
import sys
a.sort()
ans = sys.maxsize
R = 0
for L in range(n):
  while R + 1 < n and abs(a[L] - a[R]) < m:
    R += 1

  if abs(a[L] - a[R]) >= m:
    ans = min(abs(a[L] - a[R]), ans)

print(ans)