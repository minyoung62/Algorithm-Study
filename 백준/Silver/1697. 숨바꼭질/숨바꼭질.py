n, k = map(int, input().split())



answer = 0

def bfs():
    visited = [False] * 100001

    dist = [0] * 100001
    from collections import deque
    q = deque()
    q.append(n)
    visited[n] =True

    dx = [1,-1,2]
    while q:
        x = q.popleft()

        for i in range(3):
            nx = None
            if i == 2:
                nx = x * 2
            else:
                nx = x + dx[i]
            
            if nx < 0 or nx > 100000:
                continue
            
            if visited[nx] == False:
                visited[nx] = True
                dist[nx] = dist[x] + 1
               
                if nx == k :
                    return dist[nx]
                
                q.append(nx)
    return 0    

print(bfs())

        