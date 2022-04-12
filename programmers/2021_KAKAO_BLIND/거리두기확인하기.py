from collections import deque
import copy
from tabnanny import check
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(graphs, x, y):
    graph = copy.deepcopy(graphs)
    q = deque([(x, y)])
    n = len(graph)
    count = 0
    graph[x][y] = 'X'
    
    checkGraph = [[0]*5 for i in range(5)]


    while q:

        x, y = q.popleft()

        if checkGraph[x][y] >= 2:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            
            if graph[nx][ny] == 'X':
                continue

            if graph[nx][ny] == 'P':
                print(nx, ny)
                return 0
        

            if graph[nx][ny] == 'O':
                graph[nx][ny] == 'X'
                checkGraph[nx][ny] = checkGraph[x][y] + 1
                q.append((nx, ny))


    return 1
    

        


def solution(places):
    
    plen = len(places)
    n = len(places[0])
    answer = [1] * plen

    for k, place in enumerate(places):
        graph = [list(row) for row in place]
        personPostionList = []
        
        # Person 위치 탐색
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'P':
                    personPostionList.append((i,j))

        # 거리두기 확인 
        for x, y in personPostionList:

            if bfs(graph, x, y) == 0:
                answer[k] = 0
                break

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))