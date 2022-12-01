import sys
sys.setrecursionlimit(10 ** 6) # 재귀 사용할 때 필수 
input = sys.stdin.readline

n = int(input())

graph = [[] for i in range(n + 1)]

parent = [0] * (n + 1)

for i in range(n-1):
    a, b = map(int, input().split())
    graph[b].append(a)
    graph[a].append(b)


def dfs(x, par):
    for y in graph[x]:
        if y == par:
            continue
        parent[y] = x
        dfs(y, x)

dfs(1, 0)
for i in range(2, n + 1):
    print(parent[i])