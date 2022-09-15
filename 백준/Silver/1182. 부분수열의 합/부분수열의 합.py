n, s = map(int, input().split())
a = list(map(int, input().split()))
selected = []
ans = 0
def choose(cnt, total):
  global ans

  if cnt == n:

    if len(selected) !=0 and  sum(selected) == s:
      ans += 1
    return

  selected.append(a[cnt])
  choose(cnt+1, total)
  selected.pop()

  choose(cnt + 1, total + a[cnt])



choose(0, 0)

print(ans)
