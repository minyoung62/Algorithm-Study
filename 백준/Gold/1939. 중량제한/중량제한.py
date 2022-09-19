n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
for i in range(m):
  a, b, c = tuple(map(int, input().split()))
  g[a].append((b, c))
  g[b].append((a, c))
for i in range(1, n + 1):
  g[i].sort(reverse=True)
s, e =map(int, input().split())

visited = [False] * (n + 1)
from collections import deque
def isPossible(weightLimit):
  q = deque()
  q.append((s, 0))
  visited[s] = True
  
  while q:
    x, dist = q.popleft()
    if x == e:
      return True
    for x2, dist2 in g[x]:
      if not visited[x2] and weightLimit <= dist2:
        visited[x2] = True
        q.append((x2, dist2))
 


  return False
import sys
l = 1
r = 1000000001

ans = 0
while l<=r:
  mid = (l+r) // 2

  visited = [False] * (n + 1)
  if isPossible(mid):
    l = mid + 1
    ans = mid

  else:
    r = mid - 1

print(ans)
