from collections import deque

def bfs(map):
    x, y = 0, 0
    
    n = len(map)
    m = len(map[0])

    distMap = [[0] * m for i in range(n)]
    distMap[x][y] = 1
    q = deque()

    q.append((x, y))
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:

        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # map 밖인 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
                
            # 벽인 경우
            if map[nx][ny] == 0:
                continue
            
            if distMap[nx][ny] == 0:
                q.append((nx, ny))
                distMap[nx][ny] = distMap[x][y] + 1

    return distMap
def solution(maps):
    answer = 0

    distMap = bfs(maps)

    if  distMap[-1][-1] == 0 :
        return -1

    answer = distMap[-1][-1]

    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))