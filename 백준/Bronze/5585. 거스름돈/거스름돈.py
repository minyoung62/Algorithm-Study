
a = [500,100,50,10,5,1]
n = int(input())
ans = 0
n = 1000 - n
for i in range(len(a)):

  if n // a[i] != 0:
    ans += n // a[i]
    n = n % a[i]


print(ans)
