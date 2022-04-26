import sys

si = sys.stdin.readline

v, e  = tuple(map(int, si().split()))

s = int(si())
graph = [
    []
    for _ in range(v+1)
]

for i in range(e):
    a, b, cost = tuple(map(int, si().split()))
    graph[a].append((b, cost))

INF = 1e9
dist = [INF] * (v + 1)
import heapq
def d(s):
    q = []
    dist[s] = 0
    heapq.heappush(q,(0, s))

    while q:
        d, now = heapq.heappop(q)

        if dist[now] < d:
            continue
        
        for i in graph[now]:
            cost = d + i[1]

            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

d(s)
for i in dist[1:]:
    if i == INF:
        print("INF")
    else:
        print(i)