n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, list(input()))))

from collections import deque 
def bfs():
    dist = [
        [0] * m
        for _ in range(n)
    ]
    visited = [
        [False] * m
        for _ in range(n)
    ]

    q = deque()

    q.append((0,0))
    visited[0][0] = True

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

    print(dist[-1][-1] + 1)
bfs()