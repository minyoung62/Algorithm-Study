

r, c = map(int, input().split())
a = [
  list(input())
  for _ in range(r)
]

visited = [
  [False] * c
  for _ in range(r)
]

def inRange(x, y):
  return 0 <= x < r and 0 <= y <c

def canGo(x, y):
  return inRange(x, y) and not visited[x][y]

dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
ans = 0
selected = [0] * 26
def dfs(x, y, cnt):
  global ans


  for i in range(4):
    nx, ny = x + dxs[i], y + dys[i]
    if canGo(nx, ny) and selected[ord(a[nx][ny])-ord('A')] == 0:
      visited[x][y] = True
      selected[ord(a[nx][ny])-ord('A')] = 1

      dfs(nx, ny, cnt + 1)
      ans = max(ans, cnt)
      selected[ord(a[nx][ny])-ord('A')] = 0
      visited[x][y] = False

selected[ord(a[0][0])-ord('A')] =1
visited[0][0] = True
dfs(0, 0, 1)

print(ans + 1)
