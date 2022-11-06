n, m = tuple(map(int, input().split()))
a = [
  list(map(int, input().split()))
  for _ in range(n)
]
import sys
dp = [
  [-sys.maxsize] * m
  for _ in range(n)
]
left_right_dp = [
  [-sys.maxsize] * 2
  for _ in range(m)
]


dp[0][0] = a[0][0]
for i in range(1, m):
  dp[0][i] = dp[0][i-1] + a[0][i]
for i in range(1, n):
  dp[i][0] = dp[i-1][0] + a[i][0]


for i in range(1, n):
  left_right_dp[0][0] = dp[i-1][0] + a[i][0]
  for j in range(1, m):
    left_right_dp[j][0] = max(dp[i-1][j], left_right_dp[j-1][0]) + a[i][j]

  left_right_dp[-1][1] = dp[i-1][m-1] + a[i][m-1]
  for j in range(m-2, -1, -1):
    left_right_dp[j][1] = max(dp[i-1][j], left_right_dp[j+1][1]) + a[i][j]

  for j in range(m):
    dp[i][j] = max(left_right_dp[j][0], left_right_dp[j][1], dp[i][j])

print(dp[n-1][m-1])
