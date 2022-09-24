


def binary_search(s, e, nums1, num):
  while s <= e:
    mid = (s + e) // 2

    if nums1[mid] == num:
      return 1
    elif nums1[mid] < num:
      s = mid + 1
    else:
      e = mid - 1
  return 0


t = int(input())
for _ in range(t):
  n = int(input())
  n1 = list(map(int, input().split()))
  n1.sort()
  m = int(input())
  n2 = list(map(int, input().split()))
  for num in n2:
    print(binary_search(0, n - 1, n1, num))
