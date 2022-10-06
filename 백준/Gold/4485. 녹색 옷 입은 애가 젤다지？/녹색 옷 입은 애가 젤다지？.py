cnt = 0
while 1:
  n = int(input())
  cnt += 1
  if n == 0:
    break
  a = [
    list(map(int, input().split()))
    for _ in range(n)
  ]
  ca = [
    [0] * n
    for _ in range(n)
  ]
  c = 0
  for i in range(n):
    for j in range(n):
      ca[i][j] = c
      c+=1
  dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
  graph = [[] for i in range(n*n)]
  dist = [1e9] * (n*n)


  def inRange(x, y):
    return 0<= x <n and 0 <= y <n

  for i in range(n):
    for j in range(n):
      for dx, dy in zip(dxs, dys):
        nx, ny = i + dx, j + dy
        if inRange(nx, ny):
          graph[ca[i][j]].append((ca[nx][ny], a[nx][ny]))


  import heapq
  pq = [(a[0][0],0)]

  while pq:
    now_dist, x = heapq.heappop(pq)

    if now_dist > dist[x]:
      continue

    for next_x, next_dist in graph[x]:
      new_dist = now_dist + next_dist
      if new_dist < dist[next_x]:
        dist[next_x] = new_dist
        heapq.heappush(pq, (new_dist, next_x))


  print(f"Problem {cnt}: {dist[-1]}")
