n = int(input())
a = [int(input()) for _ in range(n)]

dp = [
  [0] * n,  # [0][i]위치는 (i-1)에서 온거 최댓값
  [0] * n # [1][i]위치는 (i-2)에서 온거 최댓값
]

if n == 1:
  print(a[0])
  exit()

dp[0][0], dp[0][1] = a[0], a[0] + a[1]
dp[1][1] = a[1]



for i in range(2, n):
  for j in range(2):
    if j == 0:
      dp[0][i] = dp[1][i-1] + a[i]
    else:
      dp[1][i] = max(dp[0][i-2],dp[1][i-2]) + a[i]

print(max(dp[0][n-1], dp[1][n-1]))
