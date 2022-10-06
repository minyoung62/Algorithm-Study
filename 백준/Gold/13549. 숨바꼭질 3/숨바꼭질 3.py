
n, k = map(int, input().split())
MAX_N = 100000
graph = [[] for i in range(MAX_N+1)]
dist = [0] * (MAX_N + 1)
visited = [False] * (MAX_N + 1)
def inRange(x):
  return 0 <= x <= MAX_N

for i in range(MAX_N+1):
  if inRange(i*2) and i*2 not in graph[i]:
    graph[i].append((i*2, 0))
    
  if inRange(i-1) and i-1 not in graph[i]:
    graph[i].append((i-1, 1))

  if inRange(i+1) and i+1 not in graph[i]:
    graph[i].append((i+1, 1))





ans = 0
from collections import deque
def bfs():
  if n == k:
    return
  q = deque()
  q.append(n)
  visited[n] = True
  while q:
    x = q.popleft()

    for nx, t in graph[x]:

      if not visited[nx] and inRange(x):
        visited[nx] = True
        q.append(nx)
        dist[nx] = dist[x] + t
        if nx == k:
          return


bfs()

print(dist[k])
