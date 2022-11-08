
n, m = tuple(map(int, input().split()))

a = [
  int(input())
  for _ in range(m)
]
import sys
sum_a = sum(a)

l = 1
r = sum_a



def isPossible(mid):
  cnt = 0
  for i in a:
    cnt += i // mid
    r = i % mid
    if r > 0:
      cnt += 1

  return cnt <= n

ans = 0

while l <= r:
  mid = (l + r) // 2

  if isPossible(mid):
    r = mid - 1
    ans = mid
  else:
    l = mid + 1

print(ans)
