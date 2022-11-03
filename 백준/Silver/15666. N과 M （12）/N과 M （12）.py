n, m = tuple(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
b = []

for i in range(n):
  if a[i] not in b:
    b.append(a[i])
n = len(b)

selected = []
def choose(cnt):
  if cnt == m:
    print(*selected)
    return

  for i in range(n):
    if len(selected) != 0 and selected[-1] > b[i]:
      continue
    selected.append(b[i])
    choose(cnt + 1)
    selected.pop()

choose(0)
