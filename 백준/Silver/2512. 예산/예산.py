
n = int(input())

a = list(map(int, input().split()))

budget = int(input())
import sys
l = 0
r = sys.maxsize
ans = 0

def isPossible(target):
  total = 0
  for i in range(n):
    if a[i] <= target:
      total += a[i]
    else:
      total += target

  return total <= budget

if sum(a) <= budget:
  print(max(a))
  exit(0)

while l <= r:
  mid = (l + r) // 2

  if isPossible(mid):
    ans = mid
    l = mid + 1
  else:
    r = mid - 1
print(ans)
