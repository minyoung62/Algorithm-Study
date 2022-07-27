n = int(input())

a = []
visited = []
for i in range(n):
    a.append(list(map(int, list(input()))))
    visited.append([False] * n)

from collections import deque

def inRange(x, y):
    return 0 <= x < n and 0 <= y < n

def canGo(x, y):
    return inRange(x, y) and not visited[x][y] and a[x][y] == 1

dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    cnt = 1
    while q:
        x, y = q.popleft()

        for dx ,dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if canGo(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))
                cnt += 1
    ans.append(cnt)


ans = []
for i in range(n):
    for j in range(n):

        if not visited[i][j] and a[i][j] == 1:
            bfs(i, j)

ans.sort()

print(len(ans))
for i in range(len(ans)):
    print(ans[i])
