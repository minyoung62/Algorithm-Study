
from sys import stdin
n = int(stdin.readline())


a = [
  list(map(int, stdin.readline().split()))
  for _ in range(n)
]


a1 = [[],[],[],[]]
for i in range(n):
  for j in range(4):
    a1[j].append(a[i][j])

b1 = []
b2 = dict()
for k in range(2):
  for i in range(n):
    for j in range(n):
      if k == 0:
        b1.append(a1[k][i] + a1[k+1][j])
      else:
        val = a1[k+1][i] + a1[k+2][j]
        b2[val] = b2.get(val, 0) + 1




ans = 0
for i in range(len(b1)):

  if -b1[i] in b2:

    ans += b2[-b1[i]]
print(ans)
