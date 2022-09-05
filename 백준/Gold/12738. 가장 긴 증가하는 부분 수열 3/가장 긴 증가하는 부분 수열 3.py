n = int(input())

a = list(map(int, input().split()))

dp = [a[0]]

def binaryLowwer(target):
  l = 0
  r = len(dp) - 1
  idx = len(dp)
  while l <= r:
    mid = (l + r) // 2

    if dp[mid] >= target:
      idx = mid
      r = mid - 1
    else:
      l = mid + 1

  return idx

ans = 0
for i in range(1, n):
  idx = binaryLowwer(a[i])
  if idx == len(dp):
    dp.append(a[i])
  else:
    dp[idx] = a[i]

print(len(dp))

