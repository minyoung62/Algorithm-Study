# 5 0
# -7 -3 -2 5 8

n, s = map(int, input().split())
a= list(map(int, input().split()))

ans = 0

mid = n // 2
r = a[mid:]
l = a[:mid]

dl = dict()
dr = dict()


selected = list()
isLeft = True

def insertDict(n):
  total = 0

  if len(selected) == 0:
    return
  for i in range(len(selected)):

    if isLeft:
      total += l[selected[i]]
    else:
      total += r[selected[i]]

  if isLeft:
    dl[total] = dl.get(total, 0) + 1
  else:
    dr[total] = dr.get(total, 0 ) + 1


def choose(cnt, cntNum, n):
  if cnt == n:
    insertDict(n)
    return

  selected.append(cnt)
  choose(cnt + 1, cntNum, n)
  selected.pop()

  choose(cnt + 1, cntNum + 1, n)

choose(0, 0, len(l))
isLeft = False

choose(0, 0, len(r))


for key in dr.keys():
  if key == s:
    ans += dr[key]

for key in dl.keys():
  if key == s:
    ans += dl[key]


for key in dl.keys():
  if s-key in dr:
    ans += dr[s-key] * dl[key]


print(ans)
