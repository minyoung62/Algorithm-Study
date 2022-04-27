# import sys

# si = sys.stdin.readline


# n, m = tuple(map(int, si().split()))


# indegree = [0] * (n + 1)
# graph = [
#     [] for _ in range(n + 1)
# ]

# for i in range(m):
#     a, b = tuple(map(int, si().split()))
#     graph[a].append(b)
#     indegree[b] += 1
# from collections import deque

# def topology_sort():
#     q = deque()
#     result = []

#     for i in range(1, n + 1):
#         if indegree[i] == 0:
#             q.append(i)
    
#     while q:
#         now = q.popleft()
#         result.append(now)

#         for i in graph[now]:
      
#             indegree[i] -= 1

#             if indegree[i] == 0:
#                 q.append(i)

#     for i in result:
#         print(i, end = " ")



# topology_sort()

import sys
from textwrap import indent

si = sys.stdin.readline

n, m = tuple(map(int, si().split()))

indegree = [0] * (n + 1)

graph = [
    []
    for _ in range(n + 1)
]

for i in range(m):
    pd = list(map(int, si().split()))
    for i in range(pd[0]-1):
        i += 1
        graph[pd[i]].append(pd[i+1])
        indegree[pd[i+1]] += 1

from collections import deque
def to():
    q = deque()

    result = []

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    


    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)


    if indegree.count(0) != n + 1:
        print(0)
        return

    for i in result:
        print(i)

to()