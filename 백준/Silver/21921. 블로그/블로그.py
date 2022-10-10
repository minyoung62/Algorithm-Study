
n, x = tuple(map(int, input().split()))

a =[0]+ list(map(int, input().split()))

prefix_sum = [0] *(n+1)

for i in range(1, n + 1):
  prefix_sum[i] = prefix_sum[i-1] + a[i]

ans = 0
cnt = 1
for i in range(1, n-x+2):

  if prefix_sum[i+x-1] - prefix_sum[i-1] > ans:
    ans = prefix_sum[i+x-1] - prefix_sum[i-1]
    cnt = 1
  elif prefix_sum[i+x-1] - prefix_sum[i-1] == ans:
    cnt += 1
if ans == 0:
  print("SAD")
else:
  print(ans)
  print(cnt)
