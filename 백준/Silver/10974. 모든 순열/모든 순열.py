n = int(input())
selected = []
used = [0] * (n + 1)
def choose(cnt):
  if cnt == n:
    print(*selected)
    return

  for i in range(1, n + 1):
    if used[i]:
      continue
    used[i] = 1
    selected.append(i)
    choose(cnt + 1)
    selected.pop()
    used[i] = 0

choose(0)
