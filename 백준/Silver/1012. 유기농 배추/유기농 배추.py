import sys
si = sys.stdin.readline

t = int(si())
mm = []
nn = []
kk = []

mapss=[]
for z in range(t):
    m, n, k = tuple(map(int, si().split()))
    mm.append(m)
    nn.append(n)
    kk.append(k)

    maps = [
        [0] * nn[z]
        for _ in range(mm[z])
    ]
    mapss.append(maps)

    for i in range(k):
        x, y = tuple(map(int, si().split()))
      
        mapss[z][x][y] = 1

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, visited, maps, n, m):
    q = deque()
    q.append((x, y ))
    visited[x][y] = True
    
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue

            if maps[nx][ny] == 0:
                continue

            if visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx, ny))
    
    return 1
            

for z in range(t):
    visited = [
        [0] * nn[z]
        for _ in range(mm[z])
    ]
    answer = 0
    for i in range(mm[z]):
        for j in range(nn[z]):
            
            if mapss[z][i][j] == 0 or visited[i][j] == True:
                continue
                
            answer += bfs(i, j,visited, mapss[z], nn[z], mm[z])

    print(answer)

