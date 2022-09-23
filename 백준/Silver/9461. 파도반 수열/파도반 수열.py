t = int(input())
for _ in range(t):
  n = int(input())
  dp = [1] * (101)
  dp[3], dp[4] = 2, 2
  if n <= 5:
    print(dp[n-1])
    continue
  for i in range(5,n):
    dp[i] = dp[i-1] + dp[i-5]
  
  print(dp[n-1])