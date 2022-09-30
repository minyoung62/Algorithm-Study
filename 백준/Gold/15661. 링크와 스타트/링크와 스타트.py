

n = int(input())
a = [
  list(map(int, input().split()))
  for _ in range(n)
]
selected = [0] * n
used = [0] * n
import sys
ans = sys.maxsize
def choose(cnt, cntsum):
  global ans
  if cnt == n:
    start = 0
    link = 0
    for i in range(n):
      for j in range(i+1, n):
        if selected[i] and selected[j]:
          start += a[i][j] + a[j][i]
        elif not  selected[i] and not selected[j]:
          link += a[i][j] + a[j][i]
    ans = min(ans, abs(start-link))
    return

  selected[cnt] = 1
  choose(cnt+1,cntsum + 1)
  selected[cnt] = 0

  choose(cnt+1,cntsum)


choose(0, 0)
print(ans)