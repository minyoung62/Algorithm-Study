m, n, h = map(int, input().split())

a = []

for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, input().split())))
    a.append(tmp)

visited = [
    [
    [False] * m
    for _ in range(n)
    ]
    for _ in range(h)
]
from collections import deque

dys = [1,-1,0,0,0,0]
dxs = [0,0,1,-1,0,0]
dzs = [0,0,0,0,1,-1]
q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if a[i][j][k] == 1:
                q.append((k, j, i))
                visited[i][j][k] = True

def inRange(ny, nx, nz):
    return 0 <= ny < m and 0 <= nx < n and 0 <= nz < h


while q:
    y, x, z = q.popleft()

    for dy, dx, dz in zip(dys, dxs, dzs):
        ny, nx, nz = y + dy, x + dx, z + dz
        if inRange(ny, nx, nz) and not visited[nz][nx][ny] and a[nz][nx][ny] != -1:
            visited[nz][nx][ny] = True
            q.append((ny, nx, nz))
            a[nz][nx][ny] = a[z][x][y] + 1

ans = 0
flag = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if a[i][j][k] == 0:
                flag = 1
            elif a[i][j][k] != -1:
                ans = max(a[i][j][k], ans)

if flag == 1:
    print(-1)
else:
    print(ans - 1)