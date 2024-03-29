import sys

si = sys.stdin.readline


n, m = tuple(map(int, si().split()))


indegree = [0] * (n + 1)
graph = [
    [] for _ in range(n + 1)
]

for i in range(m):
    a, b = tuple(map(int, si().split()))
    graph[a].append(b)
    indegree[b] += 1
from collections import deque

def topology_sort():
    q = deque()
    result = []

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
      
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end = " ")



topology_sort()
