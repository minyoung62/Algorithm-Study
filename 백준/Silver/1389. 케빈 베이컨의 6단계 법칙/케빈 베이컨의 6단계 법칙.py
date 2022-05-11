n, m = map(int, input().split())

graph = [
    []
    for _ in range(n + 1)
]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
car = [0] * (n + 1)
from collections import deque
def bfs(graph, dist, visited, v):
    q = deque()
    q.append(v)
    visited[v] = True

    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i] == False:
                visited[i] = True
                dist[i] = dist[x] + 1
                q.append(i)

for i in range(1, n + 1):

    dist = [0] * (n + 1)
    visited = [False] * (n + 1)
    bfs(graph, dist, visited, i)

    car[i] = sum(dist)
print(car.index(min(car[1:])))