n = int(input())

a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

# dp define
# dp[x][y] := x,y 위치가 주워졌을 때 dp[x][y]는 i,j까지 색칠한 최소 비용
dp = [[1e9, 1e9, 1e9] for _ in range(n)]

# dp init
for i in range(3):
    dp[0][i] = a[0][i]

def inRange(y):
    return 0 <= y < 3

dx = 1
# dp charge
for x in range(1, n):
    for y in range(3):        
        for dy in [-2, -1, 1, 2]:      
            
            if not inRange(y + dy):
                continue

            dp[x][y] = min(dp[x][y], dp[x-1][y + dy] + a[x][y])

# print
print(min(dp[-1]))