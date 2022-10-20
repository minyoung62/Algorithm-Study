

a, b, c = input().split()
a = list(a)[::-1]
b = list(b)[::-1]
c = list(c)[::-1]
tmp = sorted(list(set(a+b+list(c))))


ans = 0
n = len(tmp)
alen = len(a)
blen = len(b)
clen = len(c)
d = dict()
for i in range(len(tmp)):
  d[tmp[i]] = i

def isTrue():
  num1 = 0
  num2 = 0
  digit = 1
  num3 = 0
  for ch in a:
    num1 += select[d[ch]] * digit
    digit *= 10

  digit = 1
  for ch in b:
    num2 += select[d[ch]] * digit
    digit *= 10

  digit = 1
  for i in range(clen):
    num3 += select[d[c[i]]] * digit
    digit *= 10

  return num1 + num2 == num3

used = [0] * 10
select = []


def choose(cnt):
  if cnt == n:
    if isTrue():
      print("YES")
      exit(0)

    return

  for i in range(10):
    if used[i]:
      continue

    select.append(i)
    used[i] = 1
    choose(cnt + 1)
    used[i] = 0
    select.pop()

choose(0)

print("NO")
