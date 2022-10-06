
s = set()
n = int(input())
a = list(map(int, input().split()))
d = dict()
for i in range(n):
  d[a[i]] = d.get(a[i], 0) + 1

def binarySearch(target):
  l = 0
  r = n-1

  while l<=r:
    mid = (l+r)//2

    if a[mid] == target:
      return mid
    if a[mid] > target:
      r = mid -1
    else:
      l = mid + 1

  return n
a.sort()
ans = 0
for i in range(n):
  for j in range(i+1,n):
    target = a[i] + a[j]
    idx = binarySearch(target)
    if idx == n:
      continue

    if not (idx == i or idx == j) and target not in s and n > 2:
      s.add(target)
      ans += d[target]

print(ans)
