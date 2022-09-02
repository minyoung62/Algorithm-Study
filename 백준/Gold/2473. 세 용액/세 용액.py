n = int(input())
a = list(map(int, input().split()))

a.sort()

import sys
ansPos = 0
ans = sys.maxsize
for i in range(n):
  tmp = a.pop(i)
  L, R = 0, n - 2
  while L < R :
    val = a[L] + a[R]

    if ans > abs(val + tmp):
      ansPos = [tmp, a[L], a[R]]
      ans = abs(val + tmp)

    if val + tmp > 0:
      R -= 1
    else:
      L += 1

  a.insert(i, tmp)
ansPos.sort()
print(*ansPos)
