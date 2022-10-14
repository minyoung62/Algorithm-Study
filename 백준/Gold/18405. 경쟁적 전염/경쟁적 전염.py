n, m =map(int, input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int, input().split())))

doneTime, labX, labY = map(int, input().split())

tmpList = []
for i in range(n):
    for j in range(n):
        if graph[i][j] > 0:
            tmpList.append((graph[i][j],i,j))

tmpList = sorted(tmpList,key = lambda x:x[0]) 

from collections import deque
queue = deque()
for i in range(len(tmpList)):
    queue.append(tmpList[i])


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():    
    time = 0

    queue.append(tmpList.pop(0))
    while queue:
        if time == doneTime:
            return
        a= len(queue)
        for i in range(a):
            virus, x, y = queue.popleft()

            for i in range(4): #상 하 좌 우 바이러스 퍼트림
                nx = x + dx[i]
                ny = y + dy[i]

                #공간을 벗어난 경우 무시
                if nx < 0 or ny <0 or nx >= n or ny >= n:
                    continue
                #0이 아닌 곳은 무시
                if graph[nx][ny] > 0: 
                    continue
                #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y]
                    queue.append((virus,nx,ny))
                

        time+=1


bfs()
print(graph[labX-1][labY-1])
