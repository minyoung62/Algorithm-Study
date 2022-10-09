
n, m = tuple(map(int, input().split()))
a = list(map(int, input().split()))

ans = 0
ansList = []
import sys
l = 1
r = sys.maxsize

def isPossible(dist):
  global ansList
  total = []
  cnt = 0
  s =[]
  for i in range(n):
    if a[i] > dist:
      if len(s) != 0:
        total.append(s)
      total.append([a[i]])
      s = []

      continue
    if sum(s) + a[i] <= dist:
      s.append(a[i])
    else:

      total.append(s)
      s = [a[i]]

  total.append(s)

  if len(total) <= m:
    ansList = total

  return len(total) <= m

while l <= r:
  mid = (l + r) // 2

  if isPossible(mid):
    r = mid - 1

  else:
    l = mid + 1

ans = 0
for i in range(len(ansList)):
  ans = max(ans, sum(ansList[i]))

print(ans)
for i in range(len(ansList)):
  print(len(ansList[i]), end =" ")
