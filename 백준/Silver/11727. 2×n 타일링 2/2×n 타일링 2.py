n = int(input())

# dp 정의
dp = [0] * 1001

# dp init
dp[0] = 1
dp[1] = 3
dp[2] = 5

# dp full
for i in range(3, n):
    dp[i] = dp[i-1] + dp[i-2] * 2

# print
print(dp[n-1]%10007)