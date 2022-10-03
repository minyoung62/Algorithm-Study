
n, m = map(int ,input().split())
a = list(map(int, input().split()))

a.sort()
selected = []
def choose(cnt):
  if cnt == n:
    if len(selected) == m:
      print(*selected)
    return

  selected.append(a[cnt])
  choose(cnt+1)
  selected.pop()

  choose(cnt+1)

choose(0)
