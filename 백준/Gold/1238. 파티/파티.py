
import heapq

n, m, x = tuple(map(int, input().split()))
con = [[] for _ in range(n + 1)]
con2 = [[] for _ in range(n + 1)]

for i in range(m):
  u, v, cost = tuple(map(int, input().split()))
  con[v].append((u, cost))
  con2[u].append((v,cost))
ansList = [0] * (n + 1)
def dista(con):
  dist = [1e9 for _ in range(n + 1)]
  dist[x] = 0
  pq = [(0, x)]

  while pq:
    min_dist, min_index = heapq.heappop(pq)

    if min_dist > dist[min_index]:
      continue

    for target_index, target_cost in con[min_index]:
      new_dist = min_dist + target_cost

      if new_dist < dist[target_index]:
        dist[target_index] = new_dist
        heapq.heappush(pq, (new_dist, target_index))

  for i in range(1, n+1):
    ansList[i] += dist[i]

dista(con)
dista(con2)

print(max(ansList))
