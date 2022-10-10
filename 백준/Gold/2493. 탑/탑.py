
n = int(input())

a = list(map(int, input().split()))

s = [(a[0],0)]
ans = [0]*n
for i in range(1, n):

  while s:
    x, idx = s.pop()

    if x >= a[i]:
      ans[i] = idx + 1
      s.append((x, idx))
      s.append((a[i], i))
      break


  if len(s) == 0:
    ans[i] = 0
    s.append((a[i], i))
print(*ans)
