
n, m = map(int, input().split())

a = [
  list(map(int, input().split()))
  for _ in range(n)
]

homes = []
chickens = []
for i in range(n):
  for j in range(n):
    if a[i][j] == 1:
      homes.append((i,j))
    elif a[i][j] == 2:
      chickens.append((i, j))
import sys
ans = sys.maxsize
selected = []
def getLoad():
  total = 0
  for i in range(len(homes)):
    x, y = homes[i]
    mindist = sys.maxsize
    for k in range(len(selected)):
      hx, hy = selected[k]
      mindist = min(mindist, abs(x-hx) + abs(y-hy))
    total += mindist

  return total

def choose(cnt):
  global ans
  if cnt == len(chickens):
    if len(selected) == m:

      ans = min(ans, getLoad())
    return

  selected.append(chickens[cnt])
  choose(cnt + 1)
  selected.pop()

  choose(cnt + 1)



choose(0)
print(ans)