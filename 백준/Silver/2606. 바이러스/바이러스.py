n = int(input())
e = int(input())

graph = [
    []
    for _ in range(n + 1)
]
for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    answer = 0
    visited = [False] * (n + 1)

    from collections import deque

    q = deque()

    q.append(1)
    visited[1] = True

    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i] == False:
                visited[i] = True
                q.append(i)
                answer += 1
    print(answer)
bfs()