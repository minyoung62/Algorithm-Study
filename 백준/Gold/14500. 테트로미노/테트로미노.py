
n, m = tuple(map(int, input().split()))
a = [
  list(map(int, input().split()))
  for _ in range(n)
]
selected = []
dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]
visited = [
  [False] * m
  for _ in range(n)
]


def inRange(nx, ny):
  return 0 <= nx < n and 0 <= ny < m


def canGo(nx, ny):
  return inRange(nx, ny) and not visited[nx][ny]


ans = 0

selected = []
def dfs(cnt, x, y, sumVal):
  global ans
  if cnt == 4:

    ans = max(ans, sumVal)
    return

  for k in range(4):
    nx, ny = x + dxs[k], y + dys[k]
    if canGo(nx, ny):
      visited[nx][ny] = True
      dfs(cnt + 1, nx, ny, sumVal + a[nx][ny])
      visited[nx][ny] = False

      visited[nx][ny] = True
      dfs(cnt + 1, x, y, sumVal + a[nx][ny])
      visited[nx][ny] = False


for i in range(n):
  for j in range(m):
    visited[i][j] = True
    selected.append((i, j))
    dfs(1, i, j, a[i][j])
    selected.pop()
    visited[i][j] = False

print(ans)
