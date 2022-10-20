
n, m = tuple(map(int, input().split()))
a = [
  list(map(int, list(input())))
  for _ in range(n)
]
k = 1

visited = [
  [[0] * (k+1)
  for _ in range(m)]
  for _ in range(n)
]
from collections import deque
dxs, dys = [1, -1, 0, 0,], [0,0,1,-1]

def inRange(x, y):
  return 0 <= x < n and 0 <= y < m

def bfs():
  q = deque()
  q.append((0,0,0))
  visited[0][0][0] = 1


  while q:
    x, y, crashCnt = q.popleft()
    if x == n-1 and y == m-1:
      print(visited[x][y][crashCnt])
      
      exit(0)

    for dx, dy in zip(dxs, dys):
      nx, ny = x + dx, y + dy

      if inRange(nx, ny):

        if a[nx][ny] == 0 and visited[nx][ny][crashCnt] == 0: # 벽이 아닌 경우
          visited[nx][ny][crashCnt] = visited[x][y][crashCnt] + 1
          q.append((nx, ny, crashCnt))

        elif a[nx][ny] == 1 and visited[nx][ny][crashCnt] == 0:
          if crashCnt == 0: # 벽인 경우, 벽을 한번도 안 부셨을 때
            visited[nx][ny][crashCnt + 1] = visited[x][y][crashCnt] + 1
            q.append((nx, ny, crashCnt + 1))
          elif crashCnt == 1:
            continue

  print(-1)


bfs()