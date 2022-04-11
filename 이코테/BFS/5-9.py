from collections import deque


# BFS 메서드 정리
def bfs(graph, start, visited):
    q = deque([start])

    visited[start] = True

    while q:

        v = q.popleft()
        print(v, end = ' ')

        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현
visited = [False] * 9

# 정의된 DFS 함수 호출
bfs(graph, 1, visited)
