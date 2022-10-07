
n, d, k, c = tuple(map(int, input().split()))

a = [
  int(input())
  for _ in range(n)
]

sushiCountDict = dict()
l, r = 0, -1
cnt = 0
ans = 0
isFirst = True
while l !=0 or isFirst:
  isFirst = False

  while cnt != k:
    cnt += 1
    r = (r + 1) % n
    sushiCountDict[a[r]] = sushiCountDict.get(a[r], 0) + 1

  if cnt == k:
    if c in sushiCountDict:
      ans = max(ans, len(sushiCountDict.keys()))
    else:
      ans = max(ans, len(sushiCountDict.keys()) + 1)

  cnt -= 1
  if sushiCountDict[a[l]] != 0:
    sushiCountDict[a[l]] -= 1
    if (sushiCountDict[a[l]] == 0):
      del sushiCountDict[a[l]]

  l = (l + 1) % n

print(ans)
