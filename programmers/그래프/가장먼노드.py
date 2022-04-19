from collections import deque

def solution(n, edge):
    answer = 0

    graph = [[] for i in range(n + 1)]

    for i in edge:
        a, b = i[0], i[1]
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [False] * (n + 1)
    
    q = deque()
    q.append(1)
    visited[1] = True
    dist = [0] * (n + 1)

    while q:
        g = q.popleft()

        for i in graph[g]:
            
            if visited[i] == False:
        
                visited[i] = True
                dist[i] = dist[g] + 1
                q.append(i)

    answer = dist.count(max(dist))
        
    return answer
print(solution(6, [[3, 6], [4, 3],[4,5], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))