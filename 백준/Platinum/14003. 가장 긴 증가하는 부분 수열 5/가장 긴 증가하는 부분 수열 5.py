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
check =[0] * n
ans = 0
for i in range(1, n):
  idx = binaryLowwer(a[i])
  if idx == len(dp):
    check[i] = len(dp)
    dp.append(a[i])

  else:
    dp[idx] = a[i]
    check[i] = idx

ans = []
maxNum = max(check)
maxNumIdx = check.index(maxNum)
tmp = a[maxNumIdx]
ans.append(a[maxNumIdx])

for i in range(maxNumIdx - 1, -1, -1):
  if tmp > a[i] and check[maxNumIdx]-1 == check[i]:
    ans.append(a[i])
    tmp = a[i]
    maxNumIdx = i

ans.reverse()
print(len(ans))
print(*ans)