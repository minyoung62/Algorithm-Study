n = int(input())

a = list(map(int, input().split()))
a.sort()
import sys
ans = sys.maxsize
for i in range(n):

  for j in range(i+1, n):
    val1 = a[i] + a[j]

    L, R = 0, n-1
    if L == i:
      L += 1
    if L == j:
      L += 1
    if R == j:
      R -= 1
    if R == i:
      R -= 1


    while L < R:
      val2 = a[L] + a[R]

      ans = min(ans, abs(val2-val1))
      if val2 < val1:
        L += 1
        if L == i:
          L += 1
        if L == j:
          L += 1
      else:
        R -= 1
        if R == j:
          R -= 1
        if R == i:
          R -= 1

print(ans)
