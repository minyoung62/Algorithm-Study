n = int(input())
import sys
l = 1
r = n

ans = 0

def isPossible(num):
  return num * num <= n

while l <= r:
  mid = (l + r) // 2

  if isPossible(mid):
    l = mid + 1
    ans = mid
  else:
    r = mid -1
print(ans)
