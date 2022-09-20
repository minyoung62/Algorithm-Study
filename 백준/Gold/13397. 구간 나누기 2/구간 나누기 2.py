n, m = map(int, input().split())

a = list(map(int, input().split()))
import sys
ans = 0
l = 0
r = sys.maxsize
maxNum = max(a)
def isPossible(sumLimit):
  cnt = 1
  minNum = sys.maxsize
  maxNum = -sys.maxsize
  for i in range(n):

    minNum = min(minNum, a[i])
    maxNum = max(maxNum, a[i])

    if maxNum - minNum > sumLimit:
      minNum = maxNum = a[i]
      cnt += 1

  return cnt <= m

while l <= r:
  mid = (l + r) // 2

  if isPossible(mid):
    r = mid - 1
    ans = mid
  else:

    l = mid + 1
print(ans)
