
n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
selected = list()


a.sort()
selected = list()
isUsed = set()
used = [0] * 10
def choose(cnt):
  if cnt == m:
    print(*selected)
    return
  remember = -1
  for i in range(n):
    if used[i] or remember == a[i]:
      continue
    used[i] = 1
    remember = a[i]
    selected.append(a[i])
    choose(cnt+1)
    selected.pop()
    used[i] = 0


choose(0)