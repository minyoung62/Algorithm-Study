n = int(input())
a = [
  list(map(int, input().split()))
  for _ in range(n)
]
s = set()
for i in range(n):
  s.add(i)

used = [0] * n
import sys
ans = sys.maxsize
half = n // 2
selected = [0] * half
def choose(cnt):
  global ans
  if cnt == n//2:
 
    team1 = 0
    team2 = 0
    tmp =[]
    for i in range(n):
      if i not in selected:
        tmp.append(i)
    tmp2 = selected + tmp

    for i in range(half-1):
      for j in range(i+1, half):
        team1 += a[tmp2[i]][tmp2[j]] + a[tmp2[j]][tmp2[i]]
        team2 += a[tmp2[i+half]][tmp2[j+half]] + a[tmp2[j+half]][tmp2[i+half]]

    ans = min(ans, abs(team1-team2))

    return
  start = 0 if cnt == 0 else selected[cnt-1] + 1
  for x in range(start, n):

      selected[cnt] = x
      choose(cnt+1)






choose(0)

print(ans)

