
import sys
a = list(input())
orginVal = int("".join(a))
n = len(a)
selected = []
ans = sys.maxsize
used = [0] * n

def choose(cnt):
  global ans
  if cnt == n:
    val = int("".join(selected))
    if val > orginVal:
      ans = min(ans, val)

    return

  for i in range(n):
    if used[i]:
      continue
    used[i] = 1
    selected.append(a[i])
    choose(cnt+1)
    selected.pop()
    used[i] = 0


choose(0)

if ans == sys.maxsize:
  print(0)
else:
  print(ans)
