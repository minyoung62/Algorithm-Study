n, k = map(int, input().split())

wv = [(0,0)]
for i in range(n):
    w, v = map(int , input().split())
    wv.append((w, v))

dp = [[0] * (k+1) for i in range(n+1)]


for i in range(1, n + 1):
    for w in range(1, k + 1):
        
        if w < wv[i][0]:
            dp[i][w] = dp[i-1][w]
        else:

            dp[i][w] = max(dp[i-1][w], wv[i][1] + dp[i - 1][w - wv[i][0]]  )
    
    for a in dp:
        print(a)
    print()
print(dp[-1][-1])