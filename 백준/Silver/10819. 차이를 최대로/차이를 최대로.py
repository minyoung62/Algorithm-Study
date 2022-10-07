
n = int(input())
a = list(map(int, input().split()))
selected = []
used = [0] * n
ans = 0

def getSum():
  total = 0
  for i in range(1,n):
    total += abs(selected[i] - selected[i-1])
  return total
def choose(cnt):
  global ans
  if cnt  == n:

    ans = max(ans, getSum())
    return


  for i in range(n):
    if used[i]:
      continue

    used[i] = 1
    selected.append(a[i])
    choose(cnt+1)
    selected.pop()
    used[i] = 0


choose(0)

print(ans)
