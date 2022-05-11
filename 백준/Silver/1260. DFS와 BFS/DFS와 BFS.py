n, m, v = map(int, input().split())

graph = [
    []
    for _ in range(n + 1)
]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

visited = [False for _ in range(n + 1)]
from collections import deque
answer = []
def dfs(graph, v):
    
    visited[v] = True
    answer.append(v)
    print(v, end = " ")
    for i in graph[v]:
        if visited[i] == False:
            answer.append(i)
            dfs(graph, i)
dfs(graph, v)
print()


visited = [False for _ in range(n + 1)]

q = deque()
q.append(v)
visited[v] = True
answer = []
answer.append(v)
while q:
    x = q.popleft()
    for i in graph[x]:
        if visited[i] == False:
            visited[i] = True
            q.append(i)
            answer.append(i)

print(" ".join(list(map(str, answer)))) 