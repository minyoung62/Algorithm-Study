n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
from itertools import combinations
from collections import deque
virus = []
blankSpace = []
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            blankSpace.append((i, j))
        if a[i][j] == 2:
            virus.append((i, j))
ans = 0

q = deque()
tmpA = [
    [0] * m
    for i in range(n)
]
visited = [
    [False] * m
    for i in range(n)
]

dxs, dys = [1,-1,0,0], [0,0,1,-1]


def inRange(x, y):
    return 0 <= x < n and 0 <= y < m


def canGo(x, y):
    return inRange(x, y) and not visited[x][y] and tmpA[x][y] == 0

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if canGo(nx, ny):
                visited[nx][ny] = True
                tmpA[nx][ny] = 2
                q.append((nx, ny))


def countBlank():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmpA[i][j] == 0:
                cnt += 1
    return cnt

def simulation(walls):
    global ans
    # init
    for i in virus:
        q.append(i)

    for i in range(n):
        for j in range(m):
            tmpA[i][j] = a[i][j]
            visited[i][j] = False
    for i, j in walls:
        tmpA[i][j] = 1

    # bfs
    bfs()
    #
    # # count
    ans = max(countBlank(), ans)



for walls in combinations(blankSpace, 3):
    simulation(walls)

print(ans)