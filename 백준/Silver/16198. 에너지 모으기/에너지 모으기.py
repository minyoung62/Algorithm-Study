

n = int(input())
a = list(map(int, input().split()))
ans = 0
def choose(a, cnt):

  global ans
  if len(a) <= 2:
    ans = max(ans, cnt)
    return

  for i in range(1, len(a)-1):
    prefixA=a[::]
    prefixA.pop(i)
    choose(prefixA, cnt + a[i-1] * a[i+1])

choose(a, 0)

print(ans)
