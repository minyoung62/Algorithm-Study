n = int(input())
nList = list(map(int, input().split()))
m = int(input())
mList = list(map(int, input().split()))
nList.sort()

def binarySearch(target):
  l = 0
  r = n - 1
  ans = -1
  while l <= r:
    mid = (l + r) // 2
    if nList[mid] == target:
      ans = mid
      return ans
    elif nList[mid] > target:
      r = mid - 1
    else:
      l = mid + 1
  return ans

for i in range(m):

  isHave = binarySearch(mList[i])

  if isHave == -1:
    print(0)
  else:
    print(1)
