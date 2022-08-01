n, m = map(int, input().split())

a = []
visited = []
val = []
for _ in range(m):
    a.append(list(map(int, input().split())))
    visited.append([False] * n)
    val.append([0] * n)

def inRange(x, y):
    return 0 <= x < m and 0 <= y < n

def canGo(x, y):
    return inRange(x, y) and not visited[x][y] and a[x][y] == 0


from collections import deque
dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
q = deque()
def bfs():

    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if canGo(nx, ny):
                visited[nx][ny] = True
                a[nx][ny] = 1
                val[nx][ny] = val[x][y] + 1
                q.append((nx, ny))

for i in range(m):
    for j in range(n):
        if a[i][j] == 1:
            q.append((i, j))
bfs()

flag = 0
ans = 0
for i in range(m):
    for j in range(n):
        if a[i][j] == 0:
            flag = 1
        ans = max(val[i][j], ans)

if flag == 1:
    print(-1)
else:
    print(ans)