from sys import stdin

inp= stdin.readline

n  = int(inp())

m = int(inp())

graph = [
    []
    for i in range(n + 1)
]

for i in range(m):
    
    a, b, cost = tuple(map(int, inp().split()))
    graph[a].append((b, cost))


s, e = tuple(map(int, inp().split()))


INF = 1e9

dist = [INF] * (n + 1)

import heapq 

def d(s):
    h = []
    heapq.heappush(h, (s, 0))

    dist[s] = 0

    while h:
        now, d = heapq.heappop(h)
        
        if dist[now] < d:
            continue

        for i in graph[now]:
            cost = d + i[1]

            if cost < dist[i[0]] :
                dist[i[0]] = cost
                heapq.heappush(h, (i[0], cost))
        

d(s)
print(dist[e])
