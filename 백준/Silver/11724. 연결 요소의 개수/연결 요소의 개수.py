n, m = map(int, input().split())

g = [[] for i in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

ans = 0
from collections import deque
def bfs(i):
    q = deque()
    q.append(i)
    while q:
        i = q.popleft()
        for x in g[i]:
            if not visited[x]:
                visited[x] = True
                q.append(x)


for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        ans += 1
print(ans)