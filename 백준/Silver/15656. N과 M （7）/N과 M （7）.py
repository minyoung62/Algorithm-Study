
n, m = map(int ,input().split())
a = list(map(int, input().split()))

a.sort()
selected = []
def choose(cnt):
  if cnt == m:
    print(*selected)
    return
  for i in range(n):
    selected.append(a[i])
    choose(cnt+1)
    selected.pop()


choose(0)