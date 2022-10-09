
n, m = tuple(map(int, input().split()))

a = [
  list(input())
  for _ in range(n)
]

firePos = []
jPos =(1,1)
for i in range(n):
  for j in range(m):
    if a[i][j] == "F":
      firePos.append((i,j, 0))
    elif a[i][j] == "J":
      jPos= (i, j, 1)

def inRange(x, y):
  return 0 <= x < n and 0 <= y < m

visited = [
  [False] * m
  for _ in range(n)
]
dist = [
  [0] * m
  for _ in range(n)
]
ans = -1

from collections import deque
dxs, dys = [0,0,1,-1],[1,-1,0,0]
cnt = 0
def bfs():
  global cnt
  q = deque()
  for x, y, isfire in firePos:
    q.append((x, y, isfire))
    visited[x][y] = True
  q.append((jPos[0], jPos[1], 1))
  visited[jPos[0]][jPos[1]] = True


  while q:
    x, y, isJ = q.popleft()

    for dx, dy in zip(dxs, dys):
      nx, ny = x + dx, y + dy

      if inRange(nx, ny) and not visited[nx][ny] and a[nx][ny] == ".":
        if isJ == 1:

          # 현재 가려는 길에 불이 전파 되어 있지 않으면 갈 수 있음
          if a[nx][ny] != "F":
            visited[nx][ny] = True
            a[nx][ny] = "J"
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny, 1))

        elif isJ == 0 :

          visited[nx][ny] = True
          a[nx][ny] = "F"
          q.append((nx, ny, 0))

      if isJ == 1 and not inRange(nx, ny):  # 지훈이가 벽 밖으로 나왔을 때
        return dist[x][y] + 1

  return -1

def simulation():
  global ans
  # 불의 위치를 먼저 전파하면서 불의 전파 시간을 fireDist 격자 배열에 포시
  # 지훈이를 이동시켜 이동하는 거리가 불의 전파 거리보다 잛거나 같으면 이동가능 !
  ans = bfs()

simulation()

if ans == -1:
  print("IMPOSSIBLE")
else:
  print(ans)


