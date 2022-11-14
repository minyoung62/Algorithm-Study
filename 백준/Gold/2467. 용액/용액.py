n = int(input())
a = list(map(int, input().split()))

a.sort()

L, R = 0, n - 1
ans = 10 ** 10
pos = 0
while L < R:
  val = a[L] + a[R]

  if abs(val) <= ans:
    ans = abs(val)
    pos = (a[L], a[R])

  if val >= 0:
    R -= 1
  else:
    L += 1

print(pos[0], pos[1])
