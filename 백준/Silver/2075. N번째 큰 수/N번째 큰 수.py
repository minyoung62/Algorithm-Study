
n = int(input())
import heapq
pq =[]
for i in range(n):
  s =list(map(int, input().split()))

  for j in s:
    if len(pq) < n:
      heapq.heappush(pq, j)
    elif j > pq[0]:
      heapq.heappop(pq)
      heapq.heappush(pq, j)

print(pq[0])
