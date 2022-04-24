from tkinter import E


n, m = map(int, input().split())

INF = 10001
d = [INF] * 10001
d[0] = 0
coins = [0] * n
for i in range(n):
    coins[i] = int(input())

for i in range(1, m + 1):
    
    for coin in coins:
        if  d[i-coin] != INF:
            d[i] = min(d[i], d[i-coin] + 1)
        else:
            d[i] = INF



if d[m] == INF:
    print(-1)
else:
    print(d[m])
