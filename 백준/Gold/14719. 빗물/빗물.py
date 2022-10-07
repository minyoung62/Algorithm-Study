
h, w = map(int, input().split())
a = list(map(int, input().split()))

world = [
  [0] * w
  for _ in range(h)
]

for i in range(w):
  for j in range(a[i]):
    world[j][i] = 1

visited = [
  [0] * w
  for _ in range(h)
]
from collections import deque
dxs, dys = [0,0], [-1,1]

def inRange(x, y):
  return 0 <= x < h and 0 <= y < w

def bfs(x, y):
  q = deque()
  q.append((x, y))
  visited[x][y] = True
  leftRigtPos = [(x, y)]
  isOut = False
  while q:
    x, y = q.popleft()
    for dx, dy in zip(dxs, dys):
      nx, ny = x + dx, y + dy
      if inRange(nx, ny) and not visited[nx][ny] and world[nx][ny] == 0:
        visited[nx][ny] = True
        q.append((nx, ny))
        leftRigtPos.append((nx, ny))

      if not inRange(nx, ny):
        isOut = True

  if isOut:
    for x, y in leftRigtPos:
      world[x][y] = 2
  else:
    for x, y in leftRigtPos:
      world[x][y] = 3



for i in range(h):
  for j in range(w):# 2, 3
    if not visited[i][j] and world[i][j] == 0:
      bfs(i, j)
ans = 0
for i in range(h):
  for j in range(w):
    if world[i][j] == 3:
      ans += 1
print(ans)
