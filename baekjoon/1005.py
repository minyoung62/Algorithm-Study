from collections import deque

import sys
input = sys.stdin.readline

def topology_sort(v, indegree, graph, timeList, build):
    
    resultTimeList = [[] for i in range(v + 1)]

    timeList.insert(0,0)

    q = deque()
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()

        for i in graph[now]:
            indegree[i] -= 1

            resultTimeList[i].append(timeList[i] + timeList[now])

            if indegree[i] == 0:
                timeList[i] = max(resultTimeList[i])

                if build == i:
                    return timeList[i]

                q.append(i)
    
        if now == build and graph[now] == []:
            return timeList[now]

n = int(input())
Vs = [0] * n
Es = [0] * n
indegrees = []
timeLists = []
graphs = []
builds =[0] * n
for i in range(n):    
    Vs[i], Es[i] = map(int, input().split())
    timeLists.append(list(map(int, input().split())))
    indegrees.append([0] * (Vs[i] + 1))
    graphs.append([[] for i in range(Vs[i] + 1)])

    for _ in range(Es[i]):
        a, b = map(int, input().split())
        graphs[i][a].append(b)
        indegrees[i][b] += 1
    builds[i] = int(input())

for i in range(n):
    v = Vs[i]
    e = Es[i]
    indegree = indegrees[i]
    graph = graphs[i]
    timeList = timeLists[i]
    build = builds[i]

    print(topology_sort(v, indegree, graph, timeList, build))