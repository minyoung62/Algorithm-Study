
n, m = map(int ,input().split())
a = list(map(int, input().split()))
a.sort()
selected = []
used = [0] * n
def choose(cnt):
  if cnt == m:

    print(*selected)
    return

  for i in range(n):
    if used[i]:
      continue
    used[i] = 1
    selected.append(a[i])
    choose(cnt + 1)
    used[i] = 0
    selected.pop()


choose(0)
