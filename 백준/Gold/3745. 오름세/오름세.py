dp = []
a = []
def bisect_left(target):
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
while True:
  try:
    
    n = int(input())
    a = list(map(int, input().split()))
    dp = [a[0]]
  
    for j in range(1, n):
      idx = bisect_left(a[j])
  
      if idx == len(dp):
        dp.append(a[j])
      else:
        dp[idx] = a[j]
    print(len(dp))
  except:
    break