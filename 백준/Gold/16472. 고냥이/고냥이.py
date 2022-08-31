n = int(input())
a = list(input())

def canGo(R):
  if a[R + 1] not in R and len(s) < s:
    return True
  elif a[R + 1] in R:
    return True
  return False

d = dict()
for i in range(26):
  d[chr(ord('a')+i)] = 0


R = -1
ans = 0
cnt = 0
s = set()
for L in range(len(a)):
  while R + 1 < len(a) and (len(s) < n or a[R + 1] in s):

    R += 1

    s.add(a[R])
    d[a[R]] += 1

  ans = max(ans, R - L + 1)

  if d[a[L]] != 0:
    d[a[L]] -= 1

  if d[a[L]] == 0:
    s.remove(a[L])


print(ans)

