
n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
dist = [1e9] * (n + 1)

for i in range(m):
  s, e, d = tuple(map(int, input().split()))
  graph[s].append((e, d))
  graph[e].append((s,d))


import heapq
pq = [(0, 1)]
while pq:
  dist_x, x = heapq.heappop(pq)

  if dist_x > dist[x]:
    continue

  for new_x, new_dist_x in graph[x]:
    next_dist = dist_x + new_dist_x
    if next_dist < dist[new_x]:
      heapq.heappush(pq, (next_dist, new_x))
      dist[new_x] = next_dist
print(dist[n])
