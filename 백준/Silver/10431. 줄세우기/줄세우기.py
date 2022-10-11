
t = int(input())
for _ in range(t):
  tmp = list(map(int, input().split()))
  tNum = tmp[0]
  std = tmp[1:]
  ans = 0

  for i in range(len(std)):
    for j in range(i,len(std)):
      if i == j:
        continue
      if std[i] > std[j]:
        ans += 1



  print(tNum, ans)
