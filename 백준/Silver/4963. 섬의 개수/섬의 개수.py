dxs, dys = [0,0,1,-1,1,-1,-1,1],[1,-1,0,0,1,1,-1,-1]
from collections import deque

def inRange(x, y):
  return 0 <= x < h and 0<= y < w

def bfs(x, y):
  global  ans
  q = deque()
  q.append((x, y))
  visited[x][y] = True


  while q:
    x, y = q.popleft()

    for dx, dy in zip(dxs, dys):
      nx, ny = x + dx, y + dy
      if inRange(nx, ny) and not visited[nx][ny] and a[nx][ny] == 1:
        q.append((nx, ny))
        visited[nx][ny] = True



while True:
  w, h = tuple(map(int, input().split()))
  if w == 0 and h == 0:

    break
  ans = 0
  a = [
    list(map(int, input().split()))
    for _ in range(h)
  ]
  visited = [
    [False] * w
    for _ in range(h)
  ]

  for i in range(h):
    for j in range(w):
      if not visited[i][j] and a[i][j] == 1:
        bfs(i, j)
        ans += 1

  print(ans)