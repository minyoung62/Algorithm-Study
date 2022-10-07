
n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
selected = list()
isUsed = set()
used = [0] * 10
def choose(cnt, cntval):
  if cnt == m:

    tmp = "".join(list(map(str, selected)))
    if tmp not in isUsed:
      print(*selected)
      isUsed.add(tmp)
    return

  for i in range(n):
    if used[i]:
      continue
    used[i] = 1
    selected.append(a[i])
    choose(cnt+1, cntval+1)
    selected.pop()
    used[i] = 0


choose(0, 0)