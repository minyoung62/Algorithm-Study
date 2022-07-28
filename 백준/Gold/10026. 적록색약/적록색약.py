from collections import deque

n = int(input())
a = []
visited = []
for i in range(n):
    a.append(list(input()))
    visited.append([False] * n)

dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

def inRange(x, y):
    return 0 <= x < n and 0 <= y < n

def canGo(preX, preY, x, y):
    return inRange(x, y) and not visited[x][y] and a[preX][preY] == a[x][y]

def bfs(x, y, visited):

    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if canGo(x, y, nx, ny):

                visited[nx][ny] = True
                q.append((nx, ny))

def simulation(visited):
    global ans
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j, visited)
                ans += 1

ans = 0
simulation(visited)
print(ans, end=' ')

ans = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 'G':
            a[i][j] = 'R'
        visited[i][j] = False
simulation(visited)
print(ans)


