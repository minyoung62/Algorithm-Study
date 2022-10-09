
while True:
  try:
    x = int(input()) * 10000000
    n = int(input())

    a = [
      int(input())
      for _ in range(n)
    ]

    a.sort()
    ans = -1
    l, r = 0, n -1

    while l < r:
      if a[l] + a[r] < x:
        l += 1
      elif a[l] + a[r] > x:
        r -= 1
      else:
        ans = [a[l], a[r]]
        break
    # for i in range(n):
    #
    #   idx = binarySearch( x - a[i], a, len(a))
    #
    #   if idx != -1 and a[i] + a[idx] == x :
    #     ans = abs(a[i] - a[idx])
    #     ansList = [a[i], a[idx]]
    #     break

    if ans == -1:
      print("danger")
    else:

      print("yes",ans[0] ,ans[1])
  except:
    break
