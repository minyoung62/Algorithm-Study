
import sys
n, m, k  = tuple(map(int, input().split()))
a = [
  list(map(int, list(sys.stdin.readline().rstrip())))
  for _ in range(n)
]

visited = [
  [[0] * (k + 1)
  for _ in range(m)]
  for _ in range(n)
]
from collections import deque


def inRange(x, y):
  return 0 <= x < n and 0 <= y < m

def bfs():
  q = deque()
  q.append((0,0,0))
  visited[0][0][0] = 1

  dxs, dys = [1, -1, 0, 0, ], [0, 0, 1, -1]
  while q:
    x, y, crashCnt = q.popleft()

    if x == n-1 and y == m-1:
      print(visited[x][y][crashCnt])
      exit(0)


    for i in range(4):
      nx, ny = x+dxs[i], y + dys[i]

      if inRange(nx, ny) :

        if a[nx][ny] == 0 and visited[nx][ny][crashCnt] == 0: # 벽이 아닌 경우
          visited[nx][ny][crashCnt] = visited[x][y][crashCnt] + 1
          q.append((nx, ny, crashCnt))

        elif a[nx][ny] == 1 and crashCnt < k and visited[nx][ny][crashCnt+1] == 0:
            nextCrashCnt = crashCnt + 1
            visited[nx][ny][nextCrashCnt] = visited[x][y][crashCnt] + 1

            q.append((nx, ny, nextCrashCnt))


  print(-1)


bfs()

