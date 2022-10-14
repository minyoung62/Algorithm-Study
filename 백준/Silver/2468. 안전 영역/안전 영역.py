

n = int(input())
a = [
  list(map(int, input().split()))
  for _ in range(n)
]

def inRange(x, y):
  return 0 <= x < n and 0 <= y < n

from collections import deque
dxs, dys = [0,0,1,-1],[1,-1,0,0]
def bfs(water, x, y):
  q = deque()
  q.append((x, y))
  visited[x][y] = True

  while q:
    x, y = q.popleft()

    for dx, dy in zip(dxs, dys):
      nx, ny = x + dx, y + dy

      if inRange(nx, ny) and not visited[nx][ny] and a[nx][ny] > water:
        q.append((nx,ny))
        visited[nx][ny] = True

ans = 0
visited = [
  [False] * n
  for _ in range(n)
]
for water in range(101):
  for i in range(n):
    for j in range(n):
      visited[i][j] = False
  cnt = 0
  for i in range(n):
    for j in range(n):
      if not visited[i][j] and water < a[i][j]:
        bfs(water, i, j)
        cnt += 1
  ans = max(ans, cnt)

print(ans)
