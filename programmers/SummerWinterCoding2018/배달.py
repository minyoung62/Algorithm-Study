import heapq
from turtle import distance

def dj(start, graph, distance):
    
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:

            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
        
INF = 1e9

def solution(N, road, K):
    answer = 0
 
    graph = [[] for i in range(N + 1)]

    distance = [INF] * (N + 1)

    for i in range(len(road)):
        a, b, c = tuple(road[i])
        graph[a].append((b, c))
        graph[b].append((a,c))
 
    dj(1, graph, distance)

    for i in range(1, N + 1):
    
        if distance[i] == INF:
            continue
        elif distance[i] <= K:
            
            answer += 1
  

    return answer

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
#print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4))