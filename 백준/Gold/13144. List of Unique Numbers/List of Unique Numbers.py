
n = int(input())
a = list(map(int, input().split()))

r = -1
ans = 0
cnt = 0
countArr = [0] * (max(a)+1)

for l in range(n):
  while r + 1 < n and countArr[a[r+1]] == 0:
    r += 1
    countArr[a[r]] = 1

  ans += r - l + 1

  countArr[a[l]] = 0


print(ans)
