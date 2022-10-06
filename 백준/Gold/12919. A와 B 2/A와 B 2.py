
s = list(input())
t = list(input())

selected = list(s)

gap = len(t) - len(s)
ans = 0
def dfs(t):
  global ans
  if s == t:
    ans = 1
    return
  if len(t) == 0:
    return
  if (t[len(t)-1] == 'A'):
    dfs(t[:-1])
  if (t[0] == 'B'):
    dfs(t[1:][::-1])

dfs(t)

print(ans)
