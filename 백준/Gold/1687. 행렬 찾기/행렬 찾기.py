n, m = map(int, input().split())

a = [[0] * (m + 1)]
prefixSum = [[0] * (m + 1)]
for i in range(n):
  a.append([0] + list(map(int, list(input()))))
  prefixSum.append([0] * (m + 1))

for i in range(1, n+1):
  for j in range(1, m+1):
    prefixSum[i][j] = a[i][j] + prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1]


def getSum(r1, r2, i):
  return prefixSum[r2][i] - prefixSum[r2][i-1] - prefixSum[r1-1][i] + prefixSum[r1-1][i-1]


def findMaxZero(r1, r2):
  dp = [0] * (m + 1)
  for i in range(1, m + 1):
    dp[i] = getSum(r1, r2, i)
  maxZero = 0
  tmp = 0
  for i in range(1, m + 1):
    if dp[i] >= 1:
      maxZero = max(maxZero, tmp)
      tmp = 0
    else:
      tmp += 1

  maxZero = max(maxZero, tmp)
  # print(maxZero * (r2 - r1 + 1))
  return maxZero * (r2 - r1 + 1)
ans = 0

for r1 in range(1, n + 1):
  for r2 in range(r1, n + 1):

    ans = max(ans, findMaxZero(r1, r2))

print(ans)
