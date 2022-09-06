n = int(input())

a = list(map(int, input().split()))

a.sort()

L, R = 0, n - 1
import sys
ansNum = sys.maxsize
ans = 0
while L < R:
  val = a[L] + a[R]

  if ansNum > abs(val):
    ans = (a[L], a[R])
    ansNum = abs(val)

  if val > 0:
    R -= 1
  else:
    L += 1
print(ans[0], ans[1])
