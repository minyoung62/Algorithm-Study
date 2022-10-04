
n, m = map(int ,input().split())
a = list(map(int, input().split()))

a.sort()
selected = []
def choose(cnt):
  if cnt == m:
    print(*selected)
    return
  for i in range(n):
    if (len(selected) != 0 and selected[-1] > a[i]):
      continue
    selected.append(a[i])
    choose(cnt+1)
    selected.pop()


choose(0)