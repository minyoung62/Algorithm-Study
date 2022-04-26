from sys import stdin

input = stdin.readline().strip

n  = int(input())

input = stdin.readline().strip
m = int(input())

graph = [
    []
    for i in range(n + 1)
]

for i in range(m):
    
    input = stdin.readline().strip
    a, b, cost = tuple(map(int, input().split()))
    graph[a].append((b, cost))


input = stdin.readline().strip
s, e = tuple(map(int, input().split()))


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
